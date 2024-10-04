import json
import torch
import whisperx
import logging
from ts.torch_handler.base_handler import BaseHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CustomASRHandler(BaseHandler):
    def preprocess(self, data):
        audio_file = data[0].get("body").strip()
        return whisperx.load_audio(audio_file)

    def inference(self, data):
        output = self.model(data)
        return output

    def postprocess(self, inference_output):
        return inference_output["segments"]

    def handle(self, data, context):
        wav = self.preprocess(data)
        model_output = self.inference(wav)
        return self.postprocess(model_output)
