# モデルを作成するための訓練
# fine-tuningは一連のfine_tuning.pyで行うこと

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import AutoConfig, AutoModelForCausalLM, get_linear_schedule_with_warmup
from sentencepiece as spm
import json
from tqdm import tqdm

