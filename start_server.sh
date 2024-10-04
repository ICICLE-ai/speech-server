#torchserve --start --ncs --ts-config config.properties --model-store model_store --models dummy_asr=dummy_asr.mar
#torchserve --start --ncs --disable-token-auth  --model-store model_store --models dummy_asr=dummy_asr.mar
torchserve --start --ncs --disable-token-auth  --model-store model_store --models whisperx_asr=whisperx_asr.mar
