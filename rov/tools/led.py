import digital_pin

class Led(DigitalPin):

    def __init__(self, pin=16, setupWiringPi=True):
        super(self, pin, setupWiringPi)
        off()

    def on():
        super.write(0)

    def off():
        super.write(1)
