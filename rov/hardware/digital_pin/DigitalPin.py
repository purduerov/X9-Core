import wiringpi

class DigitalPin(object):
    def __init__(self, pin=16, setupWiringPi=True):
        self.pin = pin

        # sets up wiring pi gpio
        if setupWiringPi:
            wiringpi.wiringPiSetupGpio()

        # set the pin to pwm output
        wiringpi.pinMode(self.pin, wiringpi.OUTPUT)

        # keep track of current value
        self.current_value = 0

        # set to off
        self.off()

    def write(self, value):
        if value != 0:
            value = 1
        self.current_value = value

        wiringpi.digitalWrite(self.pin, value)

    def on(self):
        self.write(1)

    def off(self):
        self.write(0)

    def toggle(self):
        if self.current_value == 0:
            self.on()
        else:
            self.off()
