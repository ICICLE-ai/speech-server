import torch
import whisperx
import torch.nn as nn

class whisperXModel(nn.Module):
    #def __init__(self, size="small", device="cuda", compute="float16"):
    def __init__(self, size, device, compute):
        super(whisperXModel, self).__init__()
        self.model = whisperx.load_model(size, device, compute_type=compute, language="en")
        self.align, self.metadata = whisperx.load_align_model(language_code="en", device=device)
        self.device = device

    def forward(self, x):
        asr_results = self.model.transcribe(x, batch_size=1)
        aln_results = whisperx.align(asr_results["segments"], self.align, self.metadata, x, self.device, return_char_alignments=False)

        text = aln_results['segments'][0]['text'].strip()
        alns = aln_results['word_segments']
        return text, alns

#def model_fn(model_dir):
#    model = whisperXModel()
#    return model
