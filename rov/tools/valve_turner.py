from Adafruit_PCA9685 import PCA9685


class ValveTurner:

    ZERO_POWER = 305
    POS_MAX_POWER = 222
    NEG_MAX_POWER = 388

    def __init__(self):
        self.pin = 9#GIVE ME THE pin

        self.power = 0

        self.pwm = PCA9685()

        self.pwm.set_pwm_freq(47)

        self.pwm.set_pwm(self.pin, 0, self.ZERO_POWER)

    def rotate(self, direc):
        if(direc < 0):
            direc = -.15
        elif(direc > 0):
            direc = .15

        self.power = int((self.POW_MAX_POWER - self.ZERO_POWER) * direc)

        self.pwm.set_pwm(self.pin, 0, self.power + self.ZERO_POWER)

    def getPower(self):
        return self.power
