from time import time, sleep
from threading import Lock
import copy


from sensors import Pressure, IMU


class ROV(object):

    def __init__(self):
        self._data = {}
        self.last_update = time()

        self.simple_sensors = {
            "imu": IMU(),
            "pressure": Pressure()
        }

        self._running = True
        self._data_lock = Lock()

    @property
    def data(self):
        with self._data_lock:
            self._data['last_update'] = self.last_update
            ret = copy.deepcopy(self._data)

            return ret

    def update(self):
        with self._data_lock:
            # Update all simple sensor data and stuff it in data
            for sensor in self.simple_sensors.keys():
                self.simple_sensors[sensor].update()
                self._data[sensor] = self.simple_sensors[sensor].data

            # Our last update
            self.last_update = time()

    def run(self):
        while self._running:
            while time() - self.last_update < 0.01:
                sleep(0.005)

            self.update()

if __name__ == "__main__":
    import threading
    import json

    r = ROV()
    r_thread = threading.Thread(target=r.run)
    r_thread.daemon = True
    r_thread.start()

    while True:
        print json.dumps(r.data, indent=4)
        sleep(0.1)

