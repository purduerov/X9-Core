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
        self._data = { "t0": self.t0, "t1": self.t1, "t2": self.t2, "t3": self.t3, "t4": self.t4, "t5": self.t5, "t6": self.t6, "t7": self.t7 }

    def update_actives(self, vect8):
        self.t0.setActive(vect8.a)
        self.t1.setActive(vect8.b)
        self.t2.setActive(vect8.c)
        self.t3.setActive(vect8.d)
        self.t4.setActive(vect8.e)
        self.t5.setActive(vect8.f)
        self.t6.setActive(vect8.g)
        self.t7.setActive(vect8.h)

    def update_powers(self, vect8):
        self.t0.setPower(vect8.a)
        self.t1.setPower(vect8.b)
        self.t2.setPower(vect8.c)
        self.t3.setPower(vect8.d)
        self.t4.setPower(vect8.e)
        self.t5.setPower(vect8.f)
        self.t6.setPower(vect8.g)
        self.t7.setPower(vect8.h)

    # BMAX:TODO: Implement pushing motors to coprocessor, which will then push motors to i2c to pwm chip.
    def push_coprocessor_motors(self):
        pass

    # BMAX:TODO: Implement pushing motors directly from the pi to the i2c to pwm chip, bypassing the coprocessor.
    def push_pi_motors(self):
        pass

    def get_data(self):
        return self._data


class Thruster:
    def __init__(self):
        self.power = 0
        self.active = False

    def setActive(self, value):
        self.active = value

    def setPower(self, value):
        self.power = value
