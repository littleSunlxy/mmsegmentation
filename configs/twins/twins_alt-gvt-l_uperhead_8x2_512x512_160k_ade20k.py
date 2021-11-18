_base_ = ['twins_alt-gvt-s_uperhead_8x2_512x512_160k_ade20k.py']
model = dict(
    type='EncoderDecoder',
    pretrained='pretrained/alt_gvt_large.pth',
    backbone=dict(
        type='ALTGVT',
        embed_dims=[128, 256, 512, 1024],
        num_heads=[4, 8, 16, 32],
        depths=[2, 2, 18, 2],
        drop_path_rate=0.3),
    decode_head=dict(in_channels=[128, 256, 512, 1024]),
    auxiliary_head=dict(in_channels=512))

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=2)
