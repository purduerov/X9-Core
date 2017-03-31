class ThrusterControl(object):

    def __init__(self, thrusters, mapper, num_thrusters=8, ramp=True, max_ramp=0.01):
        self.num_thrusters = num_thrusters
        self.max_ramp = max_ramp
        self.do_ramping = ramp

        self.thrusters = thrusters
        self.mapper = mapper

        self._prev_values = None
        self._set_zero_vals()

        self._running = False

    @property
    def data(self):
        return self._prev_values

    def update(self, desired_thrust, disabled_thrusters, thruster_scales):
        if self.running:
            values = self.mapper.calculate(desired_thrust, disabled_thrusters)

            # scale thruster values by some scaler
            for i in range(self.num_thrusters):
                values[i] = values[i] * thruster_scales[i]

            if self.do_ramping:
                # check if the difference is greater than the maximum allowed
                # ramp. If it is, take the previous value and add/subtract the
                # max ramp, depending on the direction of the change.
                for i in range(self.num_thrusters):
                    if abs(values[i] - self._prev_values[i]) > self.max_ramp:
                        if values[i] > self._prev_values[i]:
                            values[i] = self._prev_values[i] + self.max_ramp
                        elif values[i] < self._prev_values[i]:
                            values[i] = self._prev_values[i] - self.max_ramp

            self.thrusters.set(values)

            self._prev_values = values
        else:
            self.thrusters.stop()

    def start(self):
        self._set_zero_vals()
        self.running = True

    def stop(self):
        self.running = False
        self._set_zero_vals()
        self.kill()

    def kill(self):
        self.thrusters.stop()

    def _set_zero_vals(self):
        self._prev_values = [0 for _ in range(self.num_thrusters)]
