Results:

The table summarises the different results with different configs.  
INSTANCE SEGMENTATION - needs a revision adding BBOX results  
 | Dataset  | Model  | Epochs  /128ROI | LR | AP result | APm | APl | Best | Time | bbox AP | bbox APm | bbox APl | model filename | 
 | :--- | :--- | :--- | :--- | :--- |  :--- | :--- | :--- | :--- | :--- | :--- |  :--- |   :--- |
 | Slight 100 - 170 | RN50 - FPN | 300 | 0.0025 | 20% |  | | | | | | |
 | Slight 199 - 293 | RN50 - FPN | 300 | 0.0025 | 32% |  | | | | | | |
 | Slight 199 - 293 | RN50 - FPN | 1500 | 0.0025 | 29% | | | | | | | |
 | Slight 199 - 293 | RN50 - FPN | 1500 | 0.00025 | 33% | 52% | 53% | X | 6m50 | | | |
 | Slight 199 - 293 | RN50 - FPN | 3000 | 0.00010 | 32%  | 51% | 53% |   | 59m   | | | |
 | Slight 199 - 293 | RN50 - FPN | 2400 / 512 | 0.00005 | 26%  | 45% | 27% |   | 51m | | | |
 | Slight 199 - 293 | RN50 - FPN | 2400 / 64 | 0.00005 | 34%  | 56% | 53% |   | 44m | | | |
 | Slight 199 - 293 | RN50 - FPN | 1500 / 64 | 0.00005 |  34%  |  56% |  53% |   | 6m50 | | | | 
 | Slight 199 - 293 | RN101 - FPN | 1500 | 0.00025 | 30% | 42% | 70% | | 42m | 29 | 42 | 78 | |
 | Slight 199 - 293 | RN101 - FPN | 1000 | 0.0025 | 31% | 48% | 85% | | 6m30 | 26% | 41% | 75% | model_IS_RN101.pth |


OBJECT DETECTION
 | Dataset  | Model  | Epochs  /128ROI | LR | AP result | APm | APl | Best | Time | file |
 | :--- | :--- | :--- | :--- | :--- |  :--- | :--- | :--- | :--- | :--- | 
 | Slight 40 - 133 | RN50 - FPN | 3000 / 128 | 0.00003 | 10% | 15% | 22% | | 2h06m | |
 | Slight 988 - 3932 | RN50 - FPN | 1500 / 128 | 0.00003 | 4% | 3.5% | 12% | | 1h0m | |
 | Slight 988 - 3932 | RN50 - FPN | 3000 / 256 | 0.00003 | 6% | 4.5% | 13% | | 2h0m |  model_final_full_256.pth |
 | Slight 988 - 3932 | RN50 - FPN | 3000 / 64 / 4 | 0.0003 | 21% | 20% | 35% | | 26m (01h03) | model_final_full_64.pth |
 | Slight 988 - 3932 | RN50 - FPN | 3000 / 64 / 4 | 0.003 | 24% | 26% | 37% | X | 2h0m (13h00m) | model_final_full_3e-3.pth |
 | Slight 988 - 3932 | RN50 - FPN | 1500 / 64 / 6 | 0.03 | 12% | 15% | 16% |  | 1h30m (15h00m) | model_final_full_3e-2.pth |
 | Slight 988 - 3932 | RN50 - FPN | 500 / 64 / 4 | 0.003 | 18% | 19% | 30% |  | 18m (18h00m) | model_finalre_full_3e-2.pth | 
 | Slight 988 - 3932 | RN50 - FPN | 500 / 64 / 4 | 0.0003 | 18% | 19% | 30% | X | 19m (18h00m) | model_finalre_full_3e-3.pth | 
 | Slight 988 - 3932 | RN101 - FPN | 1200 / 128 / 2 | 0.0025 | 22% | 23% | 37% |  | 30m (20h00m) | model_final_128.pth |
 | Slight 988 - 3932 | RN101 - FPN | 1000 / 128 / 4 | 0.00025 |  24% |  22% |  39% |  |  1h10m (21h00m) | model_r101_128x2.pth |
 | Slight 988 - 3932 | RN101 - FPN | 1000 / 128 / 4 | 0.000025 |  24% |  23% |  39% |  |  1h10m (14h00m) | model_r101_128x3.pth |
 | Slight 988 - 3932 | RN101 - FPN | 1500 / 128 / 4 | 0.00025 |  24% |  22% |  44% |  |  1h36m (16h00m) | x2 -> model_r101_128x4.pth |
 | Slight 988 - 3932 | RN101 - FPN | 1500 / 128 / 4 | 0.00015 |  25% |  22% |  43% |  |  1h36m (18h00m) | x4 -> model_r101_128x5.pth |
 | Slight 988 - 3932 | RN101 - FPN | 500 / 64 / 4 | 0.00005 |  25% |  22% |  43% | x |  1h36m (18h00m) | x5 -> model_r101_128x6.pth |
 | Slight 13k - 61k | RN101 - FPN | 4000 / 64 / 2 | 0.0025 | 17% |  27% | 40% |  |  25m (10h00m) | model_r101_ext_ODx1.pth |
 | Slight 13k - 61k | RN101 - FPN | 4000 / 64 / 2 | 0.0025 | 16% |  28% | 40% |  | 25m (10h50m) | x1 -> model_r101_ext_ODx2.pth |
 | Slight 13k - 61k | RN101 - FPN | 4000 / 128 / 2 | 0.00025 | 24% | 33% | 49% |  | 25m (11h20m) | x2 -> model_r101_ext_ODx3.pth |
 | Slight 13k - 61k | RN101 - FPN | 4000 / 128 / 2 | 0.000025 | 25% | 34% | 50% | x | 25m (12h00m) | x3 -> model_r101_ext_ODx4.pth |
 | Slight 13k - 61k | RN101 - FPN | 4000 / 128 / 2 | 0.000025 | 25% | 34% | 50% | x | 25m (12h30m) | x4 -> model_r101_ext_ODx5.pth |
 | Slight 13k - 61k | RN101 - FPN | 4000 / 128 / 2 | 0.000025 | % | % | % | x | 2h20m (16h00m) | x5 -> model_r101_ext_ODx6.pth |

