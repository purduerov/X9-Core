import numpy as np
import matplotlib.pyplot as plt


plt.axis([0,100,0,7])
plt.ion()
i = 0
while (1):
    y = 1
    x = 7
    plt.scatter(i, y)
    plt.scatter(i, x)
    i= 1+ i 
    plt.pause(0.05)
while True:
    plt.pause(0.05)

