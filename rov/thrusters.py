from Adafruit_PCA9685 import PCA9685
# using PCA9685 object:
# functions:
# set all pwm power with pwm.set_all_pwm(end_low, end_high)
# set pwm power with pwm.set_pwm(thrusterid, end_low, end_high)
#   To set PWM power % (-100% to 100%) w/ end_low and end_high: know that the
#   values don't matter, just the difference between them. The zero power
#   setting is 1.5ms high out of a 20ms period, which is 50Hz. The max
#   documented range for these T200 thrusters is 1.1ms to 1.9ms high.
#   The values we can use in this function lets us specify values between 0
#   and 4096, which are what we enter in end_low and end_high. So to get 1.5ms
#   high in a 20ms period, we set end_low=0 and end_high=310, for 4096 units
#   out of 20ms, 4096/20 = 204.8 units/ms. If we want diff for 1.5ms, we set
#   204 units/ms * 1.5ms = 307 units. This is the theoretical difference we
#   need, however under experimentation using logic analyzers, to achieve real
#   1.5 ms the difference should really be 310. So to set this 0% power, we
#   can call pwm.set_pwm(0, 0, 310) or pwm.set_pwm(0, 1024, 1334), there should
#   be no physical difference.

class Thrusters:

    ZERO_POWER = 310
    POS_MAX_POWER = 227
    NEG_MAX_POWER = 393

    def __init__(self):
        self.t0 = Thruster()
        self.t1 = Thruster()
        self.t2 = Thruster()
        self.t3 = Thruster()
        self.t4 = Thruster()
        self.t5 = Thruster()
        self.t6 = Thruster()
        self.t7 = Thruster()

        # Public segment:
        self._data = { "t0": self.t0, "t1": self.t1, "t2": self.t2, "t3": self.t3, "t4": self.t4, "t5": self.t5, "t6": self.t6, "t7": self.t7 }

        # Pi -> I2C-to-PWM variables:
        #   I2C-to-PWM Pins
        self.pins = [0, 0, 0, 0, 0, 0, 0, 0]
        #   I2C-to-PWM chip class:
        pwm = PCA9685()
        # pwm frequency should be 50Hz, but with chip inaccuracy, setting 50 is actually 53, so we set it to 47 to offset.
        pwm.set_pwm_freq(47)
        # thrusters must be set to 0 before they can be set to any other value.
        pwm.set_all_pwm(0, self.ZERO_POWER)


        # Pi -> Coprocessor variables:


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
