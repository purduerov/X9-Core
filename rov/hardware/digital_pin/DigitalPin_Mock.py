class DigitalPin_Mock(object):
    def __init__(self, pin=16, setupWiringPi=True):
        self.pin = pin

    def write(self, value):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def toggle(self):
        pass
