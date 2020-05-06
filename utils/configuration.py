from typing import Iterable
from dataclasses import dataclass


@dataclass
class System:
    seed: int = 42
    cudnn_benchmark_enabled: bool = True
    cudnn_deterministic: bool = True


@dataclass
class DataSet:
    root_dir: str = "./MoNuSAC/data"
    img_dir: str = "MoNuSAC_images_and_annotations"
    mask_dir: str = "annotations/MoNuSAC_masks_binary"
    set_dir: str = "./"
    number_of_classes: int = 4


@dataclass
class DataLoader:
    batch_size: int = 16
    num_workers: int = 6


@dataclass
class Optimizer:
    learning_rate: float = 0.00005
    momentum: float = 0.9
    weight_decay: float = 4e-5
    lr_step_milestones: Iterable = (300, )
    lr_gamma: float = 0.1


@dataclass
class Trainer:
    device: str = "cuda:0"
    epoch_num: int = 400


@dataclass
class Model:
    encoder = 'se_resnet50'
    encoder_weights = 'imagenet'
    activation = 'sigmoid'
    model_name = 'fpn'
