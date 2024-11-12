#curl -X POST http://127.0.0.1:8080/predictions/nemo_asr \
#     -H "Content-Type: text/plain" \
#     -d "/research/nfs_fosler_1/vishal/audio/slurp/slurp_real/audio-1488984199.flac"
curl -X POST http://127.0.0.1:8080/predictions/whisperx_asr \
     -H "Content-Type: text/plain" \
     -d "/home/sunder.9/icicle/server/serve/output.wav"
#curl -X POST http://127.0.0.1:8080/predictions/whisperx_asr \
#     -H "Content-Type: text/plain" \
#     -d "/tmp/tmpub4t9nj0.mp4"
#curl -X POST http://127.0.0.1:8080/predictions/my_asr \
#     -H "Content-Type: text/plain" \
#     -d "/home/sunder.9/icicle/server/serve/en_4170_185.wav"
#curl -X POST http://127.0.0.1:8080/predictions/fasterWhisper_asr \
#     -H "Content-Type: text/plain" \
#     -d "/research/nfs_fosler_1/vishal/audio/slurp/slurp_real/audio-1490109103-headset.flac"
