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
        self.locked_x = 0
        self.locked_y = 0

    def getDesired(self, direction, locked):
        desired = np.array([[0], [0], [0], [0], [0], [0]])
        desired[0, 0] = self.evalX(direction[0, 0], locked[0])
        desired[0, 1] = self.evalY(direction[0, 1], locked[1])
        desired[0, 2] = self.evalZ(direction[0, 2], locked[2])
        desired[0, 3] = self.evalPhi(direction[0, 3], locked[3])
        desired[0, 4] = self.evalMu(direction[0, 4], locked[4])
        desired[0, 5] = self.evalTheta(direction[0, 5], locked[5])

        self.locked = locked
        return desired

    def evalX(self, desired, locked):
        if locked == 0:
            return desired
        elif self.locked[0] == 1:
            return self.locked_x
        else:
            self.locked_x = desired
            return self.locked_x

    def evalY(self, desired, locked):
        if locked == 0:
            return desired
        elif self.locked[1] == 1:
            return self.locked_y
        else:
            self.locked_y = desired
            return self.locked_y

    def evalZ(self, desired, locked):
        if locked == 0:
            return desired
        elif self.locked[2] == 1:
            self.z.update(self.data.get_state())
            return self.z.getOutput()
        else:
            self.z.set_setpoint(self.data.get_state())
            return self.z.update(self.data.get_state())

    def evalPhi(self, desired, locked):
        if locked == 0:
            return desired
        elif self.locked[3] == 1:
            self.phi.update(self.data.get_state('Roll'))
            return self.phi.getOutput()
        else:
            self.phi.set_setpoint(self.data.get_state('Roll'))
            self.phi.update(self.data.get_state('Roll'))
            return self.phi.getOutput()

    def evalMu(self, desired, locked):
        if locked == 0:
            return desired
        elif self.locked[3] == 1:
            self.mu.update(self.data.get_state('Pitch'))
            return self.mu.getOutput()
        else:
            self.mu.set_setpoint(self.data.get_state('Pitch'))
            self.mu.update(self.data.get_state('Pitch'))
            return self.mu.getOutput()

    def evalTheta(self, desired, locked):
        if locked == 0:
            return desired
        elif self.locked[3] == 1:
            self.theta.update(self.data.get_state('Heading'))
            return self.theta.getOutput()
        else:
            self.theta.set_setpoint(self.data.get_state('Heading'))
            self.theta.update(self.data.get_state('Heading'))
            return self.theta.getOutput()