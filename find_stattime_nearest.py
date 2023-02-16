# -*- coding: utf-8 -*-
"""Find Stattime Nearest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ObHTe5TVkYo8MFB41n2Mzc0qEKcii5Cf
"""

import pandas as pd
import numpy as np
from google.colab import files
#Import File
master_file = pd.ExcelFile('test3.xlsx')
Test1 = pd.read_excel(master_file, 'Test1')
Test2 = pd.read_excel(master_file, 'Test2')
Test1['Index'] = pd.to_datetime(Test1['Index'])
Test2['Index'] = pd.to_datetime(Test2['Index'])
Final_Data = pd.merge_asof(Test1,Test2,on=['Index'],direction='forward')
Final_Data
Final_Data.to_csv('output.csv', encoding = 'utf-8-sig') 
files.download('output.csv')