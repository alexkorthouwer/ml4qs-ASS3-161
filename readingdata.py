# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:32:06 2020

@author: Alex Korthouwer
"""
from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
from pathlib import Path
import copy
import os
import sys
import pandas as pd
import csv

DATA_PATH = Path('./intermediate_datafiles/WISDM_ar_v1.1')
DATASET_FNAME = sys.argv[1] if len(sys.argv) > 1 else 'WISDM_ar_v1.1_raw.txt'
DATA_NAME_PREPROCESED = 'WISDM_Readable1'
DATA_NAME_PREPROCESED2 = 'WISDM_Readable2'

dataset = pd.read_csv(DATA_PATH / DATASET_FNAME,header = None ,sep = "\n")
print(len(dataset))
dataset.loc[dataset[0].str.count(',') == 6, 0] = dataset[dataset[0].str.count(',') == 6][0].str[:-1]
dataset = dataset[dataset[0].str.count(',') != 10]
dataset.to_csv(DATA_PATH /DATA_NAME_PREPROCESED, header = False, index =False, quoting=csv.QUOTE_NONE, escapechar=' ' )
dataset = pd.read_csv(DATA_PATH /DATA_NAME_PREPROCESED, header = None)
dataset =dataset.append(pd.read_csv(DATA_PATH /'temp', header = None)).reset_index(drop = True)
dataset.to_csv(DATA_PATH /DATA_NAME_PREPROCESED2, header = False)

