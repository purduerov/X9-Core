# Empty class for describing Thrusters


class Thrusters:

    def __init__(self):
        self.t0 = Thruster()
        self.t1 = Thruster()
        self.t2 = Thruster()
        self.t3 = Thruster()
        self.t4 = Thruster()
        self.t5 = Thruster()
        self.t6 = Thruster()
        self.t7 = Thruster()

class Thruster:
    def __init__(self):
        self.power = 0
        self.active = False
