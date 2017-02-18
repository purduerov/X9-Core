class Thrusters:

    def __init__(self):
        self.NUM_THRUSTERS = 8
        self.thrusters = [0 for _ in range(0, self.NUM_THRUSTERS)]
        #self._data["thrusters"] = { "actives": [], "force": [], "thrusters": {} }

    @property
    def data(self):
        return self.thrusters

    def get_data(self):
        return self.data

    def push_coprocessor_motors(self):
        pass

    def push_pi_motors(self, powers, actives):
        # Update thruster data
        for t in range(0, self.NUM_THRUSTERS):
            self.thrusters[t] = powers[t] if actives[t] else 0

    def stop(self):
        for t in range(0, self.NUM_THRUSTERS):
            self.thrusters[t] = 0
        print("EMERGENCY STOP CALLED: Thrusters have been stopped!")
