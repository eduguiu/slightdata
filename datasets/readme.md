# Introduction 

Each dataset is important since it addresses one specific problem. Therefore a description of each dataset is critical since it aims to contour the profile of each and every one of the dataset. Moreover, a To-Do list will help to define what the new Datasets will need to define. 

# Slight_ext
Slight full is a ObjectDetection (OD) composed by:
- 3 class ("Street_light", "car, "Traffic_light)
- Trainset: 11 pics and 3932 annotations (bbox)
- Testset: 63 pics and 242 annotations (bbox)
- csv-annotated file (train_labels.csv / test_labels)
Preferred models: model_r101_128x6.pth

## Slight_ext_red
Slight full is a ObjectDetection (OD) composed by:
- 3 class ("Street_light", "car, "Traffic_light)
- Trainset: 60 pics and 3932 annotations (bbox)
- Testset: 63 pics and 242 annotations (bbox)
- csv-annotated file (train_labels.csv / test_labels)
Preferred models: model_r101_128x6.pth

# Slight_full
Slight full is a ObjectDetection (OD) composed by:
- 1 class ("Street_light")
- Trainset: 988 pics and 3932 annotations (bbox)
- Testset: 63 pics and 242 annotations (bbox)
- csv-annotated file (train_labels.csv / test_labels)
Preferred models: model_r101_128x6.pth

## Slight_red
Slight full is a ObjectDetection (OD) composed by:
- 1 class ("Street_light")
- Trainset: 40 pics and 133 annotations (bbox)
- Testset: 12 pics and 56 annotations (bbox)
- csv-annotated file (train_labels.csv / test_labels)
Preferred models: 

# slight_0
Slight full is a Instance Segmentation (IS) composed by:
- 1 class ("Street_light")
- Trainset: 199 pics and 293 annotations (IS + bbox)
- Testset: 19 pics and 44 annotations (IS + Bbox)
- COCO-format json files (trainval.json on train and val on root folder) extrated from Labelme (WKentaro)
Preferred models: model_IS_RN101.pth (IS AP_large = 85% / IS AP_med = 41% )


# slight_1 (to develop)
Slight full is a Instance Segmentation (IS) composed by:
- 1 class ("Street_light" / "Pole")
- Trainset: 300 pics and 600 annotations (IS + bbox)
- Testset: 50 pics and 100 annotations (IS + Bbox)
- COCO-format json files
Preferred model: 




