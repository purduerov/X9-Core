from time import time, sleep


from threading import Lock
import copy
import numpy as np


from sensors import Pressure, IMU
from thrusters import Thrusters
from thrusters import ThrustMapper
from camera.cam import Camera


class ROV(object):

    def __init__(self, lock, data):

        self._data_lock = lock
        self._data = data

        self.last_update = time()

        self.simple_sensors = {
            "imu": IMU(),
            "pressure": Pressure()
        }

        self._running = True

        self.mapper = ThrustMapper()
        self.thrusters = Thrusters()

        #self.camera1 = Camera()
        #self.camera1.on()

    @property
    def data(self):
        with self._data_lock:
            self._data['dearclient']['last_update'] = self.last_update
            self._data['dearflask']['last_update'] = self.last_update
            ret = copy.deepcopy(self._data)

            return ret

    def update(self):
        with self._data_lock:

            #print "Update! last update was: %.5f s ago" % (time() - self.last_update)

            # Update all simple sensor data and stuff it in data
            for sensor in self.simple_sensors.keys():
                self.simple_sensors[sensor].update()
                self._data['dearclient'][sensor] = self.simple_sensors[sensor].data

            # Read controller data
            #
            # * Control Tools

            # Update all thrusters and at the end push motors:
            #
            try:
                actives = list()
                for t in self._data['dearflask']["thrusters"]:
                    actives.append([t["active"]])
                force = self._data['dearflask']["force"]
                thrust = self.mapper.generate_thrust_map(np.array(actives), np.array(force))
                self.thrusters.push_pi_motors(thrust, actives)

                self._data_lock.acquire()
                self._data['dearclient']["thrusters"]["thrusters"] = self.thrusters.get_data()
                self._data_lock.release()

            except:
                #print("ERROR: _data malformed, client may not be connected or transmitting.")
                pass

            # Our last update
            self.last_update = time()

def run(lock, data):
    rov = ROV(lock, data)
    while True:
        while time() - rov.last_update < 0.01:
#            print "waiting"
            sleep(0.005)

        rov.update()

if __name__ == "__main__":
    r = ROV()
    r._data["dearclient"]["thrusters"] = { "actives": [], "force": [], "thrusters": {} }
    r._data["dearclient"]["thrusters"]["actives"] = [1,1,1,1,1,1,1,1]
    r._data["dearclient"]["thrusters"]["force"] = [[1],[0],[0],[0],[0],[0]]
    r.run()
    # add print statement after self.update() in r.run()
