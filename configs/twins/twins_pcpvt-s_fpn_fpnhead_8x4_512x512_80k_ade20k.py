_base_ = [
    '../_base_/models/twins_pcpvt-s_fpn.py', '../_base_/datasets/ade20k.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
# model settings
norm_cfg = dict(type='SyncBN', requires_grad=True)

optimizer = dict(_delete_=True, type='AdamW', lr=0.0001, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
