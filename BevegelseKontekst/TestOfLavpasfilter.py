import serial as sr
import matplotlib.pyplot as plt
from sys import exit
import math as math
import matplotlib.animation as animation
import numpy as np
import time

serialPort = sr.Serial('COM3')

#serialString = ""  # Used to hold data coming over UART

YnMinusX = 0.0
YnMinusZ = 0.0
alpha = 0.02
g = 9.82

while True:
    # Wait until there is data waiting in the serial buffer
    
        try:
      #if (serialPort.in_waiting != 0):
        # Read data out of the buffer until a carraige return / new line is found
        
         data = serialPort.readline()
         data = data.decode('Ascii')
         list_ofdata = data.split(",")
        
      #dat=pd.read_csv("data/data5-backpack-oneshoulder.csv",names=["t","temp","accX","accY","accZ","gyroX","gyroY","gyroZ"])
        
         
        
         #print(float(list_ofdata[2])*2)
         #print("x acc")
         #print(list_ofdata)
         #print("Full data")
         
         ax = math.cos(float(list_ofdata[2])) * g
         az = math.sin(float(list_ofdata[4])) * g
         
         YnX = (1-alpha) * YnMinusX + (alpha * ax)
         YnMinusX = YnX
         YnZ = (1-alpha) * YnMinusZ + (alpha * az)
         YnMinusZ = YnZ
         
         #print(YnX, "This is YnX")
         #print(YnZ, "This is YnZ")
         
         angle = math.atan2(YnX, YnZ) #Z eller X først????
         
         print(angle, "ANGLE")

        # Print the contents of the serial data
        # print(data.decode('Ascii'))
         plt.pause(0.1)

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        
        except KeyboardInterrupt:
          exit()
        
        