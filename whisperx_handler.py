import json
import io
import os
import torch
import tempfile
import whisperx
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from whisperx_model import whisperXModel
from ts.torch_handler.base_handler import BaseHandler

class CustomASRHandler(BaseHandler):
    def initialize(self, context):
        properties = context.system_properties
        model_dir = properties.get("model_dir")

        config_path = os.path.join(model_dir, "config_wx.json")
        with open(config_path, "r") as config_file:
            config = json.load(config_file)

        size = config.get("size", "small")
        device = config.get("device", "cpu")
        compute = config.get("compute", "int8")

        self.model = whisperXModel(size, device, compute)
        self.initialized = True

    def preprocess(self, data):
        if 'data' in data[0]:
            temp_audio_path = "/tmp/temp_audio_file.wav"
            with open(temp_audio_path, 'wb') as f:
                f.write(data[0].get("data"))
            return whisperx.load_audio(temp_audio_path)

        elif 'audio' in data[0]:
            audio_data = data[0].get('audio')
            if not audio_data:
                raise ValueError("No audio data received")

            # Write the audio data directly to a temporary file
            temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")  # Adjust suffix as needed
            try:
                temp_audio_file.write(audio_data)
                print(f"Temporary file created: {temp_audio_file.name}")
                temp_audio_file.flush()

                # Load the audio directly from MP4 or Ogg format
                loaded_audio = whisperx.load_audio(temp_audio_file.name)

            except Exception as load_error:
                raise ValueError(f"Failed to load audio file: {load_error}")

            finally:
                temp_audio_file.close()
                os.remove(temp_audio_file.name)
                print(f"Temporary file deleted: {temp_audio_file.name}")

            return loaded_audio

        elif 'body' in data[0]:
            audio_file = data[0].get("body").strip()
            return whisperx.load_audio(audio_file)
        else:
            raise ValueError("No valid audio field in data.")

    def inference(self, data):
        print('TRANSCRIBING NOW')
        #print(f'DATA = {data}')
        decode, alignment = self.model(data)
        result = [{'transcription':decode, 'alignment':alignment}]
        return result

    def postprocess(self, inference_output):
        print("SERVER RESPONSE:", inference_output)
        return inference_output

    def handle(self, data, context):
        wav = self.preprocess(data)
        model_output = self.inference(wav)
        return self.postprocess(model_output)
