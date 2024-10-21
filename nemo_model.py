import torch
import torch.nn as nn
import nemo.collections.asr as nemo_asr

class nemoModel(nn.Module):
    def __init__(self, device, beam_size=1):
        super(nemoModel, self).__init__()
        print(f"LOADING MODEL")
        #self.model = nemo_asr.models.ASRModel.from_pretrained(model_name="nvidia/parakeet-tdt_ctc-110m")
        self.model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained(model_name="nvidia/parakeet-ctc-1.1b")
        print(f"MODEL LOADED")

        self.model.to(device)
        if device == 'cpu':
            torch.cuda.empty_cache()

    def forward(self, path):
        print(f"RUNNING TRANSCRIPTION")
        text = self.model.transcribe([path])[0]
        print(f"TRANSCRIPTION SUCCESSFUL")
        return {'transcription':text}
