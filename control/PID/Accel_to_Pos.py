import time


class AccelConversion(object):

        def __init__(self):
            self.time_start = time.time()

        def integration(self, accel):
            delta_t = time.time() - self.time_start
            pos = accel * (delta_t ** 2) # assumes the ROV has 0 velocity at the time of the switch to autopilot
            return pos
