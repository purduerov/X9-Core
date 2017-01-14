import sensors.SensorClass as SensorClass
import PID_controller
import numpy as np


class PID(object):
    def __init__(self):
        self.data = SensorClass.Data_file.State()
        self.controller_x = PID_controller.PID_Controller(self)
        self.controller_y = PID_controller.PID_Controller(self)
        self.controller_z = PID_controller.PID_Controller(self)
        self.controller_phi = PID_controller.PID_Controller(self)
        self.controller_mu = PID_controller.PID_Controller(self)
        self.controller_theta = PID_controller.PID_Controller(self)


    def engage_PID(self):
        updated_x = self.update_x()
        updated_y = self.update_y()
        updated_z = self.update_z()
        updated_phi = self.update_phi()
        updated_mu = self.update_mu()
        updated_theta = self.update_theta()
        return np.array([(updated_x), (updated_y), (updated_z), (updated_phi), (updated_mu), (updated_theta)])

    def update_x(self):
        self.controller_x.update(self.data.get_state())
        return self.controller_x.getOutput()

    def update_y(self):
        self.controller_y.update(self.data.get_state())
        return self.controller_y.getOutput()

    def update_z(self):
        self.controller_z.update(self.data.get_state())
        return self.controller_z.getOutput()

    def update_phi(self):
        self.controller_phi.update(self.data.get_state('Roll'))
        return self.controller_phi.getOutput()

    def update_mu(self):
        self.controller_mu.update(self.data.get_state('Pitch'))
        return self.controller_mu.getOutput()

    def update_theta(self):
        self.controller_theta.update(self.data.get_state('Heading'))
        return self.controller_theta.getOutput()

    def set_destination(self, delta_x, delta_y, delta_z, delta_phi, delta_mu, delta_theta):

        curr_x = self.data.get_state('')
        curr_y = self.data.get_state('')
        curr_z = self.data.get_state('')
        curr_phi = self.data.get_state('Roll')
        curr_mu = self.data.get_state('Pitch')
        curr_theta = self.data.get_state('Heading')

        self.dest_x = curr_x + delta_x
        self.dest_y = curr_y + delta_y
        self.dest_z = curr_z + delta_z
        self.dest_phi = curr_phi + delta_phi
        self.dest_mu = curr_mu + delta_mu
        self.dest_theta = curr_theta + delta_theta

        self.controller_x.set_setpoint(self.dest_x)
        self.controller_y.set_setpoint(self.dest_y)
        self.controller_z.set_setpoint(self.dest_z)
        self.controller_phi.set_setpoint(self.dest_phi)
        self.controller_mu.set_setpoint(self.dest_mu)
        self.controller_theta.set_setpoint(self.dest_theta)




if __name__ == '__main__':
    test = PID()

    while True:
        print(test.engage())
