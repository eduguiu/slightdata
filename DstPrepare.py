import pandas as pd
import numpy as np 
import os
import cv2
import os
from pathlib import Path
import sys
import json
from google.colab.patches import cv2_imshow

# read the annotations datasets 1M lines
df= pd.read_csv('/content/drive/My Drive/RCNN/OIDCv4_v1/csv_folder/train-annotations-bbox.csv', nrows=100000) #comment nrows to 

# Define DataFrame Annotations (DFA)
## select categories
myCategories={'/m/015qff': 'Traffic light', '/m/01mqdt' : 'Traffic sign', '/m/033rq4' : 'Street light', '/m/0h8l4fh':'Light bulb' }
myCategories2={'/m/015qff': ['Traffic light',1],
               '/m/01mqdt' : ['Traffic sign',2],
               '/m/033rq4' : ['Street light', 3], 
               '/m/0h8l4fh': ['Light bulb',4]}
               
# restrict dfa to categories2
dfa=df.loc[df['LabelName'].isin(list(myCategories2))]

# further restrict by category (Street Light)
dfa_S=dfa.loc[dfa['LabelName'] == '/m/033rq4']
dfa_S.drop(columns=['Source','IsOccluded','IsDepiction', 'IsInside', 'IsGroupOf', 'IsTruncated'], axis=1, inplace=True)

# dfa index make-up
dfa_SL = dfa_S.reset_index().rename(columns={'index': 'idx_orig'})
dfa_SL.index=range(1, len(dfa_SL)+1) 

