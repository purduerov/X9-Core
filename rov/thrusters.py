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
        self._data = { "t0": self.t0.data, "t1": self.t1.data, "t2": self.t2.data, "t3": self.t3.data, "t4": self.t4.data, "t5": self.t5.data, "t6": self.t6.data, "t7": self.t7.data }

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

    # BMAX:TODO: Implement pushing motors to coprocessor, which will then push motors to i2c to pwm chip.
    def push_coprocessor_motors(self):
        pass

    # BMAX:TODO: Implement pushing motors directly from the pi to the i2c to pwm chip, bypassing the coprocessor.
    def push_pi_motors(self, powers, actives):

    def _ramp(self):
        pass

    def get_data(self):
        return self._data


class Thruster:
    def __init__(self):
        self.data = { "active": 0, "target": 0, "current": 0, "pwm_actual": 0 }

    def setActive(self, value):
        self.data["active"] = value

    def setTarget(self, value):
        self.data["target"] = value

    def setCurrent(self, value):
        self.data["current"] = value

    def setPWMActual(self, value):
        self.data["pwm_actual"] = value
