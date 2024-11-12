model_name=whisperx_asr
rm -vrf model_store/$model_name.mar
torch-model-archiver \
    --model-name $model_name \
    --version 1.0 \
    --model-file whisperx_model.py \
    --handler whisperx_handler.py \
    --extra-files config_wx.json \
    --export-path model_store
#model_name=my_asr
#rm -vrf model_store/$model_name.mar
#torch-model-archiver \
#    --model-name $model_name \
#    --version 1.0 \
#    --model-file my_model.py \
#    --handler my_handler.py \
#    --extra-files "models.py,encoders.py,util.py,hc_ctc_all.yaml" \
#    --export-path model_store
#model_name=nemo_asr
#rm -vrf model_store/$model_name.mar
#torch-model-archiver \
#    --model-name $model_name \
#    --version 1.0 \
#    --model-file nemo_model.py \
#    --handler nemo_handler.py \
#    --extra-files config_nm.json \
#    --export-path model_store
#model_name=fasterWhisper_asr
#rm -vrf model_store/$model_name.mar
#torch-model-archiver \
#    --model-name $model_name \
#    --version 1.0 \
#    --model-file fasterWhisper_model.py \
#    --handler fasterWhisper_handler.py \
#    --extra-files config_fw.json \
#    --export-path model_store
