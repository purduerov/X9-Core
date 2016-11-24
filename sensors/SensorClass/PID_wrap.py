import Data_file
import PID_controller
import numpy as np


class PID(object):
    def __init__(self):
        self.data = Data_file.State(self)
        self.controller_x = PID_controller.PID_Controller(self)
        self.controller_y = PID_controller.PID_Controller(self)
        self.controller_z = PID_controller.PID_Controller(self)
        self.controller_phi = PID_controller.PID_Controller(self)
        self.controller_mu = PID_controller.PID_Controller(self)
        self.controller_theta = PID_controller.PID_Controller(self)
        # possible problems I forsee, it could be possible that since these are objects
        # that any attempt to call them outside of this function would return different values
        # thus it might be needed that the thrust mapping call this function to initialize zero values

    def engage(self):
        updated_x = self.update_x()
        updated_y = self.update_y()
        updated_z = self.update_z()
        updated_phi = self.update_phi()
        updated_mu = self.update_mu()
        updated_theta = self.update_theta()
        return np.array([updated_x, updated_y, updated_z, updated_phi, updated_mu, updated_theta])

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
        self.controller_phi.update(self.data.get_state())
        return self.controller_phi.getOutput()

    def update_mu(self):
        self.controller_mu.update(self.data.get_state())
        return self.controller_mu.getOutput()

    def update_theta(self):
        self.controller_theta.update(self.data.get_state())
        return self.controller_theta.getOutput()


if __name__ == '__main__':
    test = PID()

    while True:
        print(test.engage())
