import os

filewriter_path = "/tmp/finetune_alexnet/tensorboard"
checkpoint_path = '/tmp/finetune_alexnet/checkpoints'

"""
Main Part of the finetuning Script.
"""

# Create parent path if it doesn't exist
if not os.path.isdir(checkpoint_path):
    os.mkdir('tmp')
    os.mkdir('tmp/finetune_alexnet/')