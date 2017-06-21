import os
import sys

test_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_dir + "/../rov")

import time
import argparse
from hardware.motor_control import MotorControl

parser = argparse.ArgumentParser(description="Motor Movement Test")
parser.add_argument('pin', type=int, help='PWM Chip Pin [0, 15]')
parser.add_argument('power', type=float, help='Power level [-1.0, 1.0]')
parser.add_argument('time', type=float, help='How long to turn on motor (seconds)')

args = parser.parse_args()

if args.pin < 0 or args.pin > 15:
    print 'Pin must be between 0 and 15!'
    sys.exit()

if abs(args.power) > 1.0:
    print 'Power must be between -1.0 and 1.0!'
    sys.exit()

if args.time < 0.0:
    print 'Time must be non-negative!'
    sys.exit()

mc = MotorControl(
    zero_power=305,
    neg_max_power=222,
    pos_max_power=388,
    frequency=47
)

try:
    print 'Moving pin %d for %.2f seconds at %d%% power.' % (args.pin, args.time, args.power*100.0)
    mc.set(args.pin, args.power)
    time.sleep(args.time)
    mc.kill()
except KeyboardInterrupt:
    print 'Stopping test!'
    mc.kill()
    sys.exit()

