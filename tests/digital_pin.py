import os
import sys

test_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_dir + "/../rov")

import time
import argparse
from hardware.digital_pin import DigitalPin

parser = argparse.ArgumentParser(description="Digital Pin Test")
parser.add_argument('pin', type=int, help='Raspberry Pi Pin (BCM Pin)')
parser.add_argument('value', type=str, help='On or Off')

args = parser.parse_args()

dp = DigitalPin(args.pin)

if (args.value.lower() in ['false', '0', 'low', 'off']):
    dp.off()
elif (args.value.lower() in ['true', '1', 'high', 'on']):
    dp.on()
else:
    "Value not recognized (Used on or off)"
