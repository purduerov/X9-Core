from kalmanFilter import kalman
craft = kalman(10,10,10,10,10,10,10,10,10,10,10,10)
print craft.xVar
print craft.stateX
craft.update(1,1,1,1,1,1)
print craft.xVar
print craft.stateX
