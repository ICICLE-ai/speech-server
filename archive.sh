model_name=whisperx_asr
rm -vrf model_store/$model_name.mar
torch-model-archiver \
    --model-name $model_name \
    --version 1.0 \
    --model-file whisperx_model.py \
    --handler whisperx_handler.py \
    --extra-files config_wx.json \
    --export-path model_store
#model_name=fasterWhisper_asr
#rm -vrf model_store/$model_name.mar
#torch-model-archiver \
#    --model-name $model_name \
#    --version 1.0 \
#    --model-file fasterWhisper_model.py \
#    --handler fasterWhisper_handler.py \
#    --extra-files config_fw.json \
#    --export-path model_store
