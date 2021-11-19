_base_ = [
    '../_base_/models/twins_pcpvt-s_upernet.py',
    '../_base_/datasets/ade20k.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_160k.py'
]
model = dict(
    type='EncoderDecoder',
    backbone=dict(
        type='ALTGVT',
        init_cfg=dict(
            type='Pretrained', checkpoint='pretrained/alt_gvt_small.pth'),
        patch_size=4,
        embed_dims=[64, 128, 256, 512],
        num_heads=[2, 4, 8, 16],
        mlp_ratios=[4, 4, 4, 4],
        qkv_bias=True,
        norm_cfg=dict(type='LN'),
        depths=[2, 2, 10, 4],
        wss=[7, 7, 7, 7],
        sr_ratios=[8, 4, 2, 1],
        extra_norm=True,
        drop_path_rate=0.2,
        style='pytorch'),
    decode_head=dict(in_channels=[64, 128, 256, 512]),
    auxiliary_head=dict(in_channels=256))

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.00006,
    betas=(0.9, 0.999),
    weight_decay=0.01,
    paramwise_cfg=dict(custom_keys={
        'pos_block': dict(decay_mult=0.),
        'norm': dict(decay_mult=0.)
    }))

lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)

data = dict(samples_per_gpu=2, workers_per_gpu=2)