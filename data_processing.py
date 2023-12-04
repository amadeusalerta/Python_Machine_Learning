# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 05:59:52 2023

@author: efe33
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pnd
import numpy as nmpy
import matplotlib.pyplot as plt
from sklearn import preprocessing as prp
from sklearn.impute import SimpleImputer as SIT
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as STS
from sklearn.linear_model import LinearRegression as LRG

veriler=pnd.read_csv("satislar.csv")

print (veriler)

aylar=veriler[["Aylar"]]
print(aylar)

satislar=veriler[["Satislar"]]
print(satislar)

ay_satis=veriler[["Aylar","Satislar"]]
print(ay_satis)

x_train,x_test,y_    ,y_test=tts(aylar,satislar,test_size=0.33,random_state=0)

standant_calculation=STS()

x_train=standant_calculation.fit_transform(x_train)
x_test=standant_calculation.fit_transform(x_test)



