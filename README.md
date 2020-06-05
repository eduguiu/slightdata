# Slightdata - Introduction

The slightdata project aims to generate a model that is able to detect Street lights in pictures, and subsequently in videos. 
The final aim is to be able to elaborate automatised city maps with robots, video-based coupled with GPS. The database of location will be completed with categorisation tools that will adapt to client raised demands. 
Thus, the cost of doing street inventories will decrease manifolds. 

The project structures in 4 parts: 
- Swift dataset generation format-wise (COCO, VOC, custom-dictionaries etc...) for Object Detection and a 2nd Dataset to feature Classification.
  - Train/Val dataset 
  - Test dataset with 50/50 composition of Internet and selected images
- Model generation
  - Object detection
  - Instance segmentation 
  - Classification
- Metrics evaluation
  - Evaluation is made following AP metrics with special focus on being able to detect over 70% on the Test dataset
- Deployment in handheld devices and Cloud platforms
  - Adaption to Android Devices
  - Deployment into Cloud services (AWS, other...)

# Data, Data, Data

## Introduction
Make Datasets available to generate models. 

The creation of datasets comprehenses a two stepped approach:
- the first one aims to validate dataset creation processes so that the pipeline is functional. Thus, the orientation is towards a robust, bug-free process robust and dataset shallow (10's of images would usually suffice);
- the second is full fledged dataset where the core of the thing as much data as can be loaded. 

## Dataset repos 

COCOs. explain 
Imagenet. explain
LVIS. explain

## Dataset format


JSON
ImageNet
CSV (custom). 


## Dataset labelling sofware. 

There are several projects that ease the task of image labeling. The best known are
- labelImg (url: )
- labelMe (url: )




The datasets are created from images and through 
- IrfanView (1024px)
- labelme py software (CoCo json tagging)
- GColab (Jupyter Notebooks).


and loaded to be treated with Detectron2 algo notebook. 

A test is headed to change both models and weights, with newer algos, like VoV and CenterMask. 


# Models 
A model is an algorithmic structure that provides 

Main flavours. 

RCNN
ResNet-50 / 101  
[EfficientNet](https://github.com/lukemelas/EfficientNet-PyTorch)
etc...

## Architectures
Usually in architectures, the heavier, the better rule is usually enforced. Whenever the rule is broken, a breakthrough occurs. 

Template 
Architecture | Year | Common # layers | Arguments (terms / coefficients) | AP | 
ResNet
DensetNet
MobileNet

## Heads
RFP
RCNN
VoV

# What can be mesured, can be organised
Guide of different measures. 
Intro du L2, L1, etc...
AP
AP50
AP75
Metrics to apply in Object Detection 

# Deploying to production 
- Handheld devices

- Cloud/Server deployment 
  - AWS Lambda
  - Dedicated server
  




