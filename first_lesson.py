# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pnd
import numpy as nmpy
import matplotlib.pyplot as plt

veriler=pnd.read_csv("veriler.csv")

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

public list01=[1,2,3];