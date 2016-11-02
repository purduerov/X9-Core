from kalmanFilter import kalman
import matplotlib.pyplot as plt
from time import sleep
craft = kalman(10,10,10,10,10,10,10,10,10,10,10,10)
print craft.xVar
print craft.stateX
t = 0
dT =0.01
xPos = []
xPos_act = 1
craft.stateX[0]=1

xPos_act_plot =[]
vel_act = 0
while (t < 1000):
    xPos_act_plot.append(xPos_act)
    if t < 100:
        craft.update(1,1,1,1,1,1)
        vel_act = vel_act+1*dT
    elif(t <300):
        craft.update(-1,-1,-1,-1,-1,-1)
        vel_act = vel_act-1*dT
    elif(t <500):
        craft.update(1,1,1,1,1,1)
        vel_act = vel_act+1*dT
    xPos_act = xPos_act+vel_act*dT
    t = t + 1;
    xPos.append(craft.stateX[0])
    sleep(dT)

print craft.xVar
print craft.stateX[0]
plt.plot(xPos)
plt.plot(xPos_act_plot)
plt.show()

