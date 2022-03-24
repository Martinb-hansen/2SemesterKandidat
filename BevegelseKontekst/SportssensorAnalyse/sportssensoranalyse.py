# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:53:02 2022

@author: 45296
"""

import matplotlib.pyplot as plt
from sys import exit
import math as math
import matplotlib.animation as animation
import numpy as np
import time
import pandas as pd
import csv

YnMinusX = 0.0
YnMinusZ = 0.0
alpha = 0.02
g = 9.82
ax = 0.0
az = 0.0
YnX = 0.0
YnZ = 0.0
XZangle = 0.0
angle = 0.0
preangle = 0.0
samplerot = 0.0
YnRot = 0.0
newroty = 0.0
YnMinusY = 0.0
YnMinusXZ = 0.0
fs=104

# - - - - - - - - Read Files - - - - - - - 

hojreNedData = pd.read_csv("./hojrened21.csv", header=None)
hojreOpData = pd.read_csv("./hojreop21.csv", header=None)

# - - - - - - - - Højre Ned Data - - - - - - - 

HNDaccx = hojreNedData[2].values
HNDaccz = hojreNedData[4].values
HNDroty = hojreNedData[6].values

preangle = np.arctan2(HNDaccx, HNDaccz)

XZangle = (1-alpha)*YnMinusXZ+(alpha*preangle)
YnMinusXZ = XZangle

newroty = HNDroty*(1/fs)
YnRot = (1-alpha)*YnMinusY+(alpha*newroty)
YminusY = YnRot

angle = YnRot+XZangle

angle = angle*(180/3.14) #Omregning til grader

# ---------- Ret outliers - check for nye dataset ------------ #

outliers = np.where(angle > 1)

angle[outliers] = angle[outliers] - math.pi

# ------------------------------------------------------------ #

#plt.plot(angle[1000:6800])

# - - - - - - - - Init var 2 - - - - - - - 
YnMinusX2 = 0.0
YnMinusZ2 = 0.0
YnX2 = 0.0
YnZ2 = 0.0
XZangle2 = 0.0
angle2 = 0.0
preangle2 = 0.0
samplerot2 = 0.0
YnRot2 = 0.0
newroty2 = 0.0
YnMinusY2 = 0.0
YnMinusXZ2 = 0.0

# - - - - - - - - Højre Op Data - - - - - - - 
HODaccx = hojreOpData[2].values
HODaccz = hojreOpData[4].values
HODroty = hojreOpData[6].values

preangle2 = np.arctan2(HODaccx, HODaccz)

XZangle2 = (1-alpha)*YnMinusXZ2+(alpha*preangle2)
YnMinusXZ2 = XZangle2

newroty2 = HODroty*(1/fs)
YnRot2 = (1-alpha)*YnMinusY2+(alpha*newroty2)
YminusY2 = YnRot2

angle2 = YnRot2+XZangle2

angle2 = angle2*(180/3.14) #Omregning til grader

#plt.plot(angle2[1000:6800])

# -------------------------------------------------------------#



# ----------------- Summer vinkelændringer ------------------- #

sumAngle = angle2[1000:6800] - angle[1000:6800]
#sumAngle = sumAngle - np.average(sumAngle)
#plt.plot(sumAngle)

intAngle = np.zeros(sumAngle.size)
oldvalue = 0

for i in range(1, sumAngle.size):
    intAnglenew = oldvalue + sumAngle[i]
    oldValue = intAnglenew
    intAngle[i] = intAnglenew
    
plt.plot(intAngle)

# ------------------------------------------------------------ #