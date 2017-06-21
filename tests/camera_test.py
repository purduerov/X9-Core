#!/usr/bin/env python

import os
import sys

test_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(test_dir + "/../rov")

import time
from camera.cameras import Cameras

cameras = Cameras()

try:
    cameras.start()

    while True:
        c_status = cameras.status()
        for c in c_status:
            print ""
            print "Name:   %s" % c
            print "Status: %s" % c_status[c]['status']
            print "Port:   %s" % c_status[c]['port']

        time.sleep(2)
except KeyboardInterrupt:
    print 'Stopping test!'
    cameras.kill()
    sys.exit()
