Results:

The table summarises the different results obtained in Segmentation category. 

 | Dataset  | Model  | Epochs  /128ROI | LR | AP result | APm | APl | Best | Time |
 | :--- | :--- | :--- | :--- | :--- |  :--- | :--- | :--- | :--- |
 | Slight 100 - 170 | RN50 - FPN | 300 | 0.0025 | 20% |  | | | |
 | Slight 199 - 293 | RN50 - FPN | 300 | 0.0025 | 32% |  | | | |
 | Slight 199 - 293 | RN50 - FPN | 1500 | 0.0025 | 29% | | | | |
 | Slight 199 - 293 | RN50 - FPN | 1500 | 0.00025 | 33% | 52% | 53% | X | 6m50 | 
 | Slight 199 - 293 | RN50 - FPN | 3000 | 0.00010 | 32%  | 51% | 53% |   | 59m   | 
 | Slight 199 - 293 | RN50 - FPN | 2400 / 512 | 0.00005 | 26%  | 45% | 27% |   | 51m | 
 | Slight 199 - 293 | RN50 - FPN | 2400 / 64 | 0.00005 | 34%  | 56% | 53% |   | 44m | 
 | Slight 199 - 293 | RN50 - FPN | 1500 / 64 | 0.00005 |  34%  |  56% |  53% |   | 6m50 | 
 | Slight 199 - 293 | RN101 - FPN | 1500 | 0.00025 | 30% | 42% | 70% | | 42m |
 | Slight 199 - 293 | RN101 - FPN | 300 | 0.0025 | 33% | | | | |


OBJECT DETECTION
 | Dataset  | Model  | Epochs  /128ROI | LR | AP result | APm | APl | Best | Time |
 | :--- | :--- | :--- | :--- | :--- |  :--- | :--- | :--- | :--- |
 | Slight 40 - 133 | RN50 - FPN | 3000 / 128 | 0.00003 | 10% | 15% | 22% | | 2h06m |
 | Slight 988 - 3932 | RN50 - FPN | 1500 / 128 | 0.00002 | 4% | 3.5% | 12% | | 1h0m |
 | Slight 988 - 3932 | RN50 - FPN | 3000 / 256 | 0.00003 | 6% | 4.5% | 13% | | 2h0m |
 | Slight 988 - 3932 | RN50 - FPN | 3000 / 256 | 0.00003 | 6% | 4.5% | 13% | | 2h0m |
