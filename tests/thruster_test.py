import os
import sys

test_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_dir + "/../rov")

import time
from hardware.motor_control import MotorControl

mc = MotorControl(
    zero_power=305,
    neg_max_power=222,
    pos_max_power=388,
    frequency=47
)

thrusters = [
    ("Front Left H",   7),
    ("Front Right H",  4),
    ("Back Left H",    6),
    ("Back Right H",   5),

    ("Front Left V",  10),
    ("Front Right V",  0),
    ("Back Left V",   11),
    ("Back Right V",   1),
]

power = 0.2

try:
    for thruster in thrusters:
        time.sleep(1)
        print "Spinning %s" % thruster[0]
        mc.set(thruster[1], power)
        time.sleep(1)
        mc.set(thruster[1], 0)
        time.sleep(0.5)
        mc.set(thruster[1], -power)
        time.sleep(1)
        mc.set(thruster[1], 0)
    mc.kill()
except KeyboardInterrupt:
    print 'Stopping thrusters!'
    mc.kill()
    sys.exit()

