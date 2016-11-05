import thrust_mapper
import overseer
import printer
import Vectors


"""what is this initialized to"""
"""Rampticker ="""

"""implement initEverything here use i^2c and wiringPi"""
thruster = [int] * 8
receiveState = 255
voltage = [int] * 8
current = [int] * 8

Overseer = overseer.Overseer()

"""fast int here called RampTicker"""

test = 0

thruster = Vectors.vect8(1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500)
RampTicker = 0
while True:

    Overseer.checkForUpdate()
    thruster = Overseer.updateFromThrusters()

    if RampTicker >= 20:
        Overseer.doRamping()
        RampTicker = 0


    """print out the values in thruster via the i2c pwm"""


    """is this necessary without the can
    for x in range(0, 8):
        printer.printString("\nThrusters:\n")
        printer.printString("0: ")
        printer.printInt()"""
    RampTicker += 1


def MAX(x, y):
    if x > y:
        return x
    return y


def MIN(x, y):
    if x > y:
        return y
    return x
