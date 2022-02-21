import serial as sr
import matplotlib.pyplot as plt
from sys import exit
import math as math
import matplotlib.animation as animation
import numpy as np
import time
import pandas as pd
import csv

serialPort = sr.Serial('COM3')
serialPort2 = sr.Serial('COM5')

#serialString = ""  # Used to hold data coming over UART

# YnMinusX = 0.0
# YnMinusZ = 0.0
# alpha = 0.02
# g = 9.82

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

f = open('textout.csv', 'w')
writer = csv.writer(f)

while True:
    # Wait until there is data waiting in the serial buffer
    
        try:
            
            
            # - - - - - - - - Potentiometer - - - - - - - 
            data1 = serialPort2.readline()
            data1 = data1.decode('Ascii')
            
            list_ofdata = data1.split("\t")
            
            inp = float(list_ofdata[0])
            
            
            #print("POTEN", (inp-173)/3.77)
            
            # - - - - - - - - Potentiometer - - - - - - - 
            
        
            data = serialPort.readline()
            data = data.decode('Ascii')
            list_ofdata = data.split(",")
        
         
           # ax = math.cos(float(list_ofdata[2])) * g
           # az = math.sin(float(list_ofdata[4])) * g
         
            # YnX = (1-alpha) * YnMinusX + (alpha * ax)
            # YnMinusX = YnX
            # YnZ = (1-alpha) * YnMinusZ + (alpha * az)
            # YnMinusZ = YnZ

            # angle = math.atan2(YnX, YnZ) #Z eller X først????
         
            # print(angle, "ANGLE")
            
            # data1 = pd.read_csv('data9.csv', sep= ',', header=None)
            # data1.columns = ["Sample", "Temperature [°C]",  "accX", "accY", "accZ", "rotX", "rotY", "rotZ"]
            # accx = data1['accX']
            # accz = data1['accZ']
            # roty = data1['rotY']
            accx = float(list_ofdata[2])
            accz = float(list_ofdata[4])
            roty = float(list_ofdata[6])
            
            preangle = math.atan2(accx, accz)
        
            XZangle = (1-alpha)*YnMinusXZ+(alpha*preangle)
            YnMinusXZ = XZangle
            
            newroty = roty*(1/fs)
            YnRot = (1-alpha)*YnMinusY+(alpha*newroty)
            YminusY = YnRot
        
            angle = YnRot+XZangle
            
        #plt.plot(preangle) #Vinkel i radianer
        #plt.plot(YnRot) #radianer 
       
            angle = angle*(180/3.14)
            #plt.plot(angle)
            #plt.show()
            print("ANGLE", angle+116, "POTEN", (inp-173)/3.77)
            
            wrut = ([angle+116, (inp-173)/3.77])
            
            writer.writerow(wrut)
            
        
        except KeyboardInterrupt:
          exit()
          f.close()
        
        