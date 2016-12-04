from kalmanFilter import kalman
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
craft = kalman(5,5,10,5,10,10,10,10,10,10,10,10);
t = 0
dT =0.01
zPos = []
yPos = []
tPos = []
xPos = []
xPos_act = 1
tPos_act = 1
zPos_act = 1
yPos_act = 1


zPos_act_plot =[]
xPos_act_plot =[]
yPos_act_plot =[]
tPos_act_plot =[]
vel_act = 0
while (t < 1000):
    craft.update()

    print (craft.est_pos());

    t = t + 1;
    zPos.append(craft.increase+craft.noiseZ*np.random.random())
    yPos.append(craft.increase+craft.noiseY*np.arctan(np.random.random()))
    tPos.append(craft.increase+craft.noiseT*np.random.random())
    xPos.append(craft.increase+craft.noiseX*np.arctan(np.random.random()))

    zPos_act_plot.append(craft.stateZ[0])
    xPos_act_plot.append(craft.stateX[0])
    tPos_act_plot.append(craft.stateT[0])
    yPos_act_plot.append(craft.stateY[0])
    sleep(dT)

plt.plot(xPos)
plt.plot(xPos_act_plot)
"""
plt.plot(tPos)
plt.figure(2)
plt.plot(tPos_act_plot)
"""
plt.show()

