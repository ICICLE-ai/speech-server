import json
import io
import os
import torch
from fasterWhisper_model import whisperFModel
from ts.torch_handler.base_handler import BaseHandler

class CustomASRHandler(BaseHandler):
    def initialize(self, context):
        properties = context.system_properties
        model_dir = properties.get("model_dir")

        config_path = os.path.join(model_dir, "config_fw.json")
        with open(config_path, "r") as config_file:
            config = json.load(config_file)

        size = config.get("size", "small")
        device = config.get("device", "cpu")
        compute = config.get("compute", "int8")

        self.model = whisperFModel(size, device, compute)
        self.initialized = True

    def preprocess(self, data):
        if 'data' in data[0]:
            temp_audio_path = "/tmp/temp_audio_file.wav"
            with open(temp_audio_path, 'wb') as f:
                f.write(data[0].get("data"))
            return temp_audio_path

        audio_file = data[0].get("body").strip()
        return audio_file

    def inference(self, data):
        output = self.model(data)
        return output

    def postprocess(self, inference_output):
        return [inference_output]

    def handle(self, data, context):
        wav = self.preprocess(data)
        model_output = self.inference(wav)
        return self.postprocess(model_output)
