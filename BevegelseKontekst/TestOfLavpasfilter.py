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

f = open('Megadataset.csv', 'w')
writer = csv.writer(f)

while True:
    # Wait until there is data waiting in the serial buffer
    
        try:
            
            
            # - - - - - - - - Potentiometer - - - - - - - 
            
            #serialPort2.flushInput() 
            data1 = serialPort2.readline()
            data1 = data1.decode('Ascii')
            
            list_ofdata = data1.split("\t")
            
            
            inp = float(list_ofdata[0])
            
            
           # print("POTEN", (inp-173)/3.77)
            
            # - - - - - - - - Potentiometer - - - - - - - 
            
            #  - - - sportssensor - - -- - 
            
            serialPort.flushInput() 
            data = serialPort.readline()
            data = data.decode('Ascii')
            list_ofdata = data.split(",")
        
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
       
            angle = angle*(180/3.14) #Omregning til grader
            
            #  - - - sportssensor - - -- - 

            print("ANGLE", angle+116, "POTEN", (inp-173)/3.77)
            
            wrut = ([angle+116, (inp-173)/3.77])
            
            writer.writerow(wrut)
            
            #plt.pause(0.02083333) #fs på 48 hz
            
            #SIDEN VI IKKE FLUSHER POTENTIOMETER; STYRES SAMPLINGEN AF DEN (48 hz)
            
        
        except KeyboardInterrupt:
          exit()
          f.close()
        
        