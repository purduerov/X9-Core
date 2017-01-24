import time

class Accel_to_Pos(object):

        def integration(self, accel):
            delta_t = time.time() - self.time_start
            pos = accel * (delta_t ** 2) # assumes the ROV has 0 velocity at the time of the switch to autopilot
            return pos

        def start_over(self):
            self.time_start = time.time()
