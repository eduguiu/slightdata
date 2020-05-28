'''
this function aims to get all the images of a folder and generate a xxx_labels.csv file that contains all the annotations: 
- filename, class, height, width, xmin, xmax, ymin, ymax
This is used to feed a BBox-based Object Detection like Detectron2 algorithm. in order to train a model which will 
catch Street Lights. 
'''

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

# read size of image DF Pictures (dfp)
def createDFP(direct, categ='Street light'):
    '''
    this function generates the DataFrame of all the images within, returns img_ix, filename, Height and Width.
    the input is a working str with the folder path containing images. 
    ver 2.0
    '''
    LST=[]
    ls=[]
    # list all the files present in the folder Direct
    ls = sorted([k for k in os.listdir(direct) if 'jpg' in k])
    for i in range(len(ls)): 
        fn = os.path.join(direct + '/' + ls[i])
        im = cv2.imread(fn)
        h,w,_ = im.shape
        dictL = {'idx_img':i+1,
                'ImageID': ls[i].rstrip(".jpg"),
                 'height': h,
                 'width': w,
                 'class': categ}
        LST.append(dictL)
    dfp= pd.DataFrame(LST)
    return dfp

folder = '/content/drive/My Drive/RCNN/OIDCv4_v1/Dataset/test/Street light'
dfp_SL = createDFP(folder)

# second version of the merge DF 
def Merge_DF(dfa, dfp):
    ''' pass on the df Annotations and the df Pictures in folder. 
    this function gives back a merged df with all the annotations to the present 
    pictures with id, Height, width, and real postion of BBOX
    '''
    df_F = dfa.merge(dfp[['ImageID', 'idx_img', 'height', 'width', 'class']],
                  on = 'ImageID' ,
                  how = 'inner', 
                  suffixes=("_Ann", "_Pic"))
    # the index is reset to start at position 1. 
    df_F.index=range(1, len(df_F)+1)

    df_F['xmin']= (df_F['XMin'] * df_F['width']).astype(int)
    df_F['xmax']= (df_F['XMax'] * df_F['width']).astype(int)
    df_F['ymin']= (df_F['YMin'] * df_F['height']).astype(int)
    df_F['ymax']= (df_F['YMax'] * df_F['height']).astype(int)

    # drop useless columns
    df_F.drop(columns=['Confidence', 'XMin', 'YMin', 'XMax', 'YMax'], inplace=True)
    
    return df_F
  
# ============== MERGE dfa & dfp ================
df_Dst = Merge_DF(dfa_SL, dfp_SL)

# == df output preparation, columns renaming, 
df_out = df_Dst.drop(columns=['idx_orig', 'idx_img', 'LabelName']).rename(columns={'ImageID': 'filename'})
df_out['filename'] = df_out['filename'].apply(lambda x: f"{x}.jpg")

# ============== write data to csv file ===========
df_out.to_csv('/content/drive/My Drive/RCNN/OIDCv4_v1/Dataset/test/Street light/test_labels.csv', header=True)

