from time import time, sleep
from threading import Lock
import copy


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

        self.mapper = ThrustMapper()
        self.thrusters = Thrusters()

        self._data_lock = Lock()

    @property
    def data(self):
        self._data_lock.acquire()

        self._data['last_update'] = self.last_update
        ret = copy.deepcopy(self._data)

        self._data_lock.release()

        return ret

    def update(self):
        self._data_lock.acquire()

        print "Update! last update was: %.5f s ago" % (time() - self.last_update)

        # Update all simple sensor data and stuff it in data
        for sensor in self.simple_sensors.keys():
            self.simple_sensors[sensor].read()
            self._data[sensor] = self.simple_sensors[sensor].data

        # Update all thrusters and at the end push motors:
        #
        # actives = self._data["thrusters"]["actives"]
        # force = self._data["thrusters"]["force"]
        # thrust = mapper.generate_thrust_map(np.array(actives), np.array([[0],[0],[0],[0],[0],[0]]))
        # self.thrusters.push_pi_motors(actives)
        # self._data["thrusters"]["thrusters"] = thrusters.get_data()

        # Our last update
        self.last_update = time()

        self._data_lock.release()

    def run(self):
        while True:
            while time() - self.last_update < 0.1:
                sleep(0.05)

            self.update()




if __name__ == "__main__":
    r = ROV()
    r.run()
