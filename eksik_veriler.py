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

veriler=pnd.read_csv("eksikveriler.csv")

print (veriler)

boy=veriler[["boy"]]
print(boy)

boy_kilo=veriler[["boy","kilo"]]
print(boy_kilo)

class humans:
         boy=170;
         def running(self,b):
             return b+10;
ali = humans()
print(ali.boy)
print(ali.running(90))

#Eksik Veriler

from sklearn.impute import SimpleImputer

imputer=SimpleImputer(missing_values=nmpy.nan,strategy='mean')

yaslar=veriler.iloc[:,1:4].values
print(yaslar)
imputer=imputer.fit(yaslar[:,1:4])
yaslar[:,1:4]=imputer.transform(yaslar[:,1:4])
print(yaslar)