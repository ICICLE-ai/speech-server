import torch
import whisperx
import torch.nn as nn

class whisperXModel(nn.Module):
    def __init__(self, size="large-v3", device="cuda", compute="float16"):
        super(whisperXModel, self).__init__()
        self.model = whisperx.load_model(size, device, compute_type=compute, language="en")

    def forward(self, x):
        txt = self.model.transcribe(x, batch_size=1)
        return txt

def model_fn(model_dir):
    model = whisperXModel()
    return model
