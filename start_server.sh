export TMPDIR=/local/scratch
torchserve --start --ncs --disable-token-auth  --ts-config config.properties --model-store model_store --models nemo_asr=nemo_asr.mar
#torchserve --start --ncs --disable-token-auth  --model-store model_store --models whisperx_asr=whisperx_asr.mar
#torchserve --start --ncs --disable-token-auth  --model-store model_store --models fasterWhisper_asr=fasterWhisper_asr.mar
