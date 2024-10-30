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
        #if 'data' in data[0]:
        #    temp_audio_path = "/tmp/temp_audio_file.wav"
        #    with open(temp_audio_path, 'wb') as f:
        #        f.write(data[0].get("data"))
        #    return whisperx.load_audio(temp_audio_path)

        #audio_file = data[0].get("body").strip()
        #return whisperx.load_audio(audio_file)

        if 'data' in data[0]:
            temp_audio_path = "/tmp/temp_audio_file.wav"
            with open(temp_audio_path, 'wb') as f:
                f.write(data[0].get("data"))
            return whisperx.load_audio(temp_audio_path)

        elif 'audio' in data[0]:
            # Extract the audio bytearray from the HTTP request
            audio_data = data[0].get('audio')

            if not audio_data:
                raise ValueError("No audio data received")

            # Convert the byte array into a BytesIO stream
            audio_stream = io.BytesIO(audio_data)

            # Use pydub to convert Ogg/Opus to WAV
            try:
                # Load Ogg/Opus audio using pydub
                audio = AudioSegment.from_file(audio_stream, format="ogg")

                # Save the audio temporarily as a WAV file
                temp_wav_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                audio.export(temp_wav_file.name, format="wav")
                temp_wav_file.close()  # Close the file so it can be read by the model

                print(f'NAME OF FILE : {temp_wav_file.name}')
                return whisperx.load_audio(temp_wav_file.name)

            except Exception as e:
                raise ValueError(f"Failed to process audio stream: {e}")

        audio_file = data[0].get("body").strip()
        return whisperx.load_audio(audio_file)

    def inference(self, data):
        print('TRANSCRIBING NOW')
        #print(f'DATA = {data}')
        decode, alignment = self.model(data)
        result = [{'transcription':decode, 'alignment':alignment}]
        return result

    def postprocess(self, inference_output):
        print("SERVER RESPONSE:", inference_output)
        return inference_output
        #response = {
        #    "statusCode": 200,
        #    "headers": {
        #        "Content-Type": "application/json",
        #        "Access-Control-Allow-Origin": "*",  # Allow requests from any origin
        #        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        #        "Access-Control-Allow-Headers": "Content-Type",
        #    },
        #    "body": inference_output[0]
        #}
        #return [response]

    def handle(self, data, context):
        wav = self.preprocess(data)
        model_output = self.inference(wav)
        return self.postprocess(model_output)
