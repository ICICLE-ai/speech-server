import torch
from faster_whisper import WhisperModel
import torch.nn as nn

class whisperFModel(nn.Module):
    def __init__(self, size, device, compute):
        super(whisperFModel, self).__init__()
        self.model = WhisperModel(size, device=device, compute_type=compute)

    def forward(self, x):
        segments, info = self.model.transcribe(x, beam_size=5)
        segment = list(segments)[0]
        start = segment.start
        end = segment.end
        text = segment.text.strip()
        return {'start':start, 'end':end, 'text':text}
