# Slightdata - Introduction

The slightdata project aims to generate a model that is able to detect Street lights in pictures, and subsequently in videos. 
The final aim is to be able to elaborate automatised city maps with robots, video-based coupled with GPS. The database of location will be completed with categorisation tools that will adapt to client raised demands. 
Thus, the cost of doing street inventories will decrease manifolds. 

The project structures in 4 parts: 
- Swift dataset generation format-wise (COCO, VOC, custom-dictionaries etc...) for Object Detection and a 2 Dataset to make Classification functions. 
  - Train/Val dataset 
  - Test dataset with 50/50 composition of Internet and selected images
- Model generation
  - Object detection
  - Instance segmentation 
  - Classification
- Metrics evaluation
  - Evaluation is made following AP metrics with special focus on being able to detect over 70% on the Test dataset. 
- Deployment in handheld devices and Cloud platforms. 
  - 

Make Datasets available to generate Detectron2 models. 

The datasets are created from images and through 
- IrfanView (1024px)
- labelme py software (CoCo json tagging)
- GColab (Jupyter Notebooks).

and loaded to be treated with Detectron2 algo notebook. 

A test is headed to change both models and weights, with newer algos, like VoV and CenterMask. 

