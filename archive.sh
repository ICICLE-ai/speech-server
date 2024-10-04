model_name=whisperx_asr
rm -vrf model_store/$model_name.mar
torch-model-archiver \
    --model-name $model_name \
    --version 1.0 \
    --model-file whisperx_model.py \
    --handler whisperx_handler.py \
    --export-path model_store
#torch-model-archiver \
#    --model-name dummy_asr \
#    --version 1.0 \
#    --model-file dummy_model.py \
#    --serialized-file dummy_asr_model.pth \
#    --handler custom_asr_handler.py \
#    --export-path model_store
