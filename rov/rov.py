from time import time, sleep
from threading import Lock
import copy
import numpy as np


from sensors import Pressure, IMU
from thrusters import Thrusters
from thrust_mapper import ThrustMapper


class ROV(object):

    def __init__(self):
        self._data = {}
        self.last_update = time()

        self.simple_sensors = {
            "imu": IMU(),
            "pressure": Pressure()
        }

        self._running = True

        self.mapper = ThrustMapper()
        self.thrusters = Thrusters()

        self._data_lock = Lock()

    @property
    def data(self):
        with self._data_lock:
            self._data['last_update'] = self.last_update
            ret = copy.deepcopy(self._data)

            return ret

    def update(self):
        with self._data_lock:

            print "Update! last update was: %.5f s ago" % (time() - self.last_update)

            # Update all simple sensor data and stuff it in data
            for sensor in self.simple_sensors.keys():
                self.simple_sensors[sensor].update()
                self._data[sensor] = self.simple_sensors[sensor].data

            # Read controller data
            #
            # * Make thruster's force vector
            # * Control Tools


            # Update all thrusters and at the end push motors:
            #
            actives = self._data["thrusters"]["actives"]
            thrust = self.mapper.generate_thrust_map(np.array(actives), np.array(force))
            self.thrusters.push_pi_motors(thrust, actives)
            self._data["thrusters"]["thrusters"] = self.thrusters.get_data()

            # Our last update
            self.last_update = time()

    def run(self):
        while self._running:
            while time() - self.last_update < 0.01:
                sleep(0.005)

            self.update()

if __name__ == "__main__":
    r = ROV()
    r._data["thrusters"] = { "actives": [], "force": [], "thrusters": {} }
    r._data["thrusters"]["actives"] = [1,1,1,1,1,1,1,1]
    r._data["thrusters"]["force"] = [[1],[0],[0],[0],[0],[0]]
    r.run()
    # add print statement after self.update() in r.run()
