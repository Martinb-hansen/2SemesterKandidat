
import matplotlib.pyplot as plt
import numpy as np


data = np.array([])
b = np.array([[22], [33], [44]])

data = np.append(data, float(b[2]))
data1 = np.append([float(b[0])], [float(b[1])], [float(b[2])])  # b[2] = xacc b[4] = acc b[6] = yrot

ax = data1[0][0]
print(ax)











