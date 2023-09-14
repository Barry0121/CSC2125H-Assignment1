# -*- coding: utf-8 -*-
"""
    :author: LAVIS (with modification from Barry Xue and Shiyuan Feng)
    :url: https://github.com/salesforce/LAVIS
    :copyright: Copyright (c) 2022 Salesforce, Inc.
    :license: BSD 3-Clause License.
"""

import torch
from PIL import Image
from lavis.models import load_model_and_preprocess

# setup device to use (TODO: might be a bad idea...)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_caption_tools(name='blip_caption', model_type='base_coco'):
    """
    Triggers pretrained model loading

    :param name: default to 'blip_caption'
    :param model_type: default to 'base_coco'
        You can find detail configuration at 'LAVIS/lavis/configs/models/[model_name+model_type].yaml'.
        You can provide URL or local file path to corresponding model weights (Check: https://opensource.salesforce.com/LAVIS/latest/tutorial.configs.html).
    :return: PyTorch Model, Preprocessing tool
    """

    # load model, first time loading might take a while
    # I downloaded the cache file, and put it at 'LAVIS/model_base_capfilt_large.pth';
    # I also changed the default config file, which always pull from url to system cache.
    # The config file I changed: 'LAVIS/lavis/configs/models/blip_caption_base_coco.yaml'
    model, vis_processors, _ = load_model_and_preprocess(name=name, model_type=model_type, is_eval=True, device=device)
    return model, vis_processors


def caption_image(model, vis_processors, image_path):
    """
    Process the image with given model and processors

    :param model:
    :param vis_processors:
    :param iamge:
    :param pretrain_path:
    :return: str, caption related to the given image.
    """
    # process the image
    raw_image = Image.open(image_path).convert("RGB")
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    # generate the caption
    caption = model.generate({"image": image})
    return caption[0]