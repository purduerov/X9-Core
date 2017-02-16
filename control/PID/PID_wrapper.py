import sensors.SensorClass as SensorClass
import PID_controller
import numpy as np


class PID(object):

    def __init__(self):
        self.data = SensorClass.Data_file.State()
        self.locked = [0, 0, 0, 0, 0, 0]
        self.x = 0
        self.y = 0
        self.z = PID_controller.PID_Controller()
        self.phi = PID_controller.PID_Controller()
        self.mu = PID_controller.PID_Controller()
        self.theta = PID_controller.PID_Controller()
        self.prevOut = np.array([[0], [0], [0], [0], [0], [0]])

    def getDesired(self, direction, locked):
        desired = np.array([[0], [0], [0], [0], [0], [0]])
        desired[0, 0] = self.evalStatisLock(direction[0, 0], locked[0], self.locked[0],
                                            self.prevOut[0, 0])
        desired[0, 1] = self.evalStatisLock(direction[0, 1], locked[1], self.locked[1],
                                            self.prevOut[0, 1])

        self.locked = locked
        self.prevOut = desired

    def evalStatisLock(self, desired, locked, prevLockStatus, prevOut):
        if locked == 0:
            return desired
        elif prevLockStatus == 1:
            return prevOut
        else:
            return desired

    def evalAbsoluteLock(self):
