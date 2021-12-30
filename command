#####
train
#####

python tools/train.py configs/swin/upernet_swin_tiny_patch4_window7_512x512_160k_ade20k.py --options model.pretrained=/root/data/Swin-TF/imagenet_pretrined/swin_tiny_patch4_window7_224.pth model.backbone.use_checkpoint=True

####
test
####
python tools/test.py <CONFIG_FILE> <SEG_CHECKPOINT_FILE> --eval mIoU  --show --show-dir
