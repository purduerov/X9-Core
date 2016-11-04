from kalmanFilter import kalman
import matplotlib.pyplot as plt
from time import sleep
craft = kalman(10,10,10,10,10,10,10,10,10,10,10,10);
t = 0
dT =0.01
xPos = []
xPos_act = 1
craft.stateX[0]=0

xPos_act_plot =[]
vel_act = 0
while (t < 1000):
    xPos_act_plot.append(xPos_act)
    if t < 100:
        craft.update()
        vel_act = vel_act+1*dT
    elif(t <300):
        craft.update()
        vel_act = vel_act-1*dT
    elif(t <500):
        craft.update()
        vel_act = vel_act+1*dT
    xPos_act = xPos_act+vel_act*dT
    print (craft.stateX);
    t = t + 1;
    xPos.append(craft.stateX[0])
    sleep(dT)

plt.plot(xPos)
plt.plot(xPos_act_plot)
plt.show()

