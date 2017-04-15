class ValveTurner(object):
    def __init__(self, motor_control, pin):
        self.pin = pin
        self.motor_control = motor_control

    def rotate(self, power):
        self.motor_control.set(self.pin, power)
