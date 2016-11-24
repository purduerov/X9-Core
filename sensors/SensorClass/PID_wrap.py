import Data_file
import PID_controller


class PID(object):
    def __init__(self):
        self.data = Data_file.State(self)
        self.controller_x = PID_controller.PID_Controller(self)
        self.controller_y = PID_controller.PID_Controller(self)
        self.controller_z = PID_controller.PID_Controller(self)
        self.controller_phi = PID_controller.PID_Controller(self)
        self.controller_mu = PID_controller.PID_Controller(self)
        self.controller_theta = PID_controller.PID_Controller(self)

    def engage(self):
        updated_x = self.update_x()
        updated_y = self.update_y()
        updated_z = self.update_z()
        updated_phi = self.update_phi()
        updated_mu = self.update_mu()
        updated_theta = self.update_theta()

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
