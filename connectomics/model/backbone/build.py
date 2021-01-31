from __future__ import print_function, division
from typing import Optional, List

import torch
import torch.nn as nn
from .resnet import ResNet3D
from .repvgg import RepVGG3D
from ..utils.misc import IntermediateLayerGetter

backbone_dict = {
    'resnet': ResNet3D,
    'repvgg': RepVGG3D,
}

def build_backbone(backbone_type: str, 
                   feat_keys: List[str],
                   **kwargs):
    assert backbone_type in ['resnet', 'repvgg']
    return_layers = {'layer0': feat_keys[0],
                     'layer1': feat_keys[1], 
                     'layer2': feat_keys[2],
                     'layer3': feat_keys[3],
                     'layer4': feat_keys[4]}    

    backbone = backbone_dict[backbone_type](**kwargs)
    assert len(feat_keys) == backbone.num_stages
    return IntermediateLayerGetter(backbone, return_layers)