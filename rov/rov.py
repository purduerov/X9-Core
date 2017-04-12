from time import time, sleep
import traceback
import sys

from threading import Lock
import copy
import numpy as np


from sensors import Pressure, IMU
from thrusters import Thrusters
from thrusters import ThrustMapper
from camera.cam import Camera
from tools import Claw, ValveTurner


class ROV(object):

    def __init__(self, lock, data):

        self._data_lock = lock
        self._data = data
        self.dearclient = {"thrusters": {}, "tools": {}}

        self.last_update = time()

        self.simple_sensors = {
            "imu": IMU(),
            "pressure": Pressure()
        }

        self._running = True

        self.mapper = ThrustMapper()
        self.thrusters = Thrusters()

        self.camera1 = Camera()
        self.camera1.on()

        self.claw = Claw()
        self.valve = ValveTurner()

    @property
    def data(self):
        with self._data_lock:
            #self._data['dearclient']['last_update'] = self.last_update
            self._data['dearflask']['last_update'] = self.last_update
            self.dearclient['last_update'] = self.last_update
            self._data['dearclient'] = self.dearclient
            ret = copy.deepcopy(self._data)

            return ret

    def update(self):
        with self._data_lock:

            #print "Update! last update was: %.5f s ago" % (time() - self.last_update)

            # Update all simple sensor data and stuff it in data
            for sensor in self.simple_sensors.keys():
                self.simple_sensors[sensor].update()
                #self._data['dearclient'][sensor] = self.simple_sensors[sensor].data
                self.dearclient[sensor] = self.simple_sensors[sensor].data
                #print self.simple_sensors[sensor].data
                #print self._data['dearclient']
                #print "UPDATE!"

            # Read controller data
            #
            # * Control Tools

            # Update all thrusters and at the end push motors:
            #
            try:
                actives = list()
                force = list()

                t = ["t7", "t0", "t4", "t3", "t6", "t1", "t5", "t2"] # The order the Thrust mapping algorithm will see FR -> clockwise
                f = ["x", "y", "z", "roll", "pitch", "yaw"]

                #print 'Looping over thrusters for active list'
                for x in t:
                    actives.append(self._data['dearflask']['thrusters'][x]['active'])

                for m in f:
                    force.append(self._data['dearflask']['force'][m])

                thrust = self.mapper.generate_thrust_map(np.array(actives), np.array(force) * 1.5)

                print "Thrust:"
                print thrust.tolist()[0]
                self.thrusters.push_pi_motors(thrust.tolist()[0], actives)
                #print self._data['dearflask']['thrusters']['t6']

                #self._data['dearclient']["thrusters"]["thrusters"] = self.thrusters.get_data()
                self.dearclient["thrusters"] = self.thrusters.get_data()

                print self._data["dearflask"]["tools"]["claw"]
                print self._data["dearflask"]["tools"]["valve"]

                self.claw.grab(self._data["dearflask"]["tools"]["claw"])
                self.valve.rotate(self._data["dearflask"]["tools"]["valve"])

                self.dearclient["tools"]["claw"] = self.claw.getPower()
                self.dearclient["tools"]["valve"] = self.valve.getPower()

            except TypeError as err:
                print err
            except:
                i = sys.exc_info()
                print i[0]
                print i[1]
                traceback.print_tb(i[2], limit=1, file=sys.stdout)

            # Our last update
            self._data['dearclient'] = self.dearclient
            self.last_update = time()

def run(lock, data):
    rov = ROV(lock, data)
    #with lock:
    #    dearflask = {rov.thrusters.get_data(), "force": {}}
    #    data["dearflask"] = dearflask
    while True:
        while time() - rov.last_update < 0.01:
            sleep(0.005)

        rov.update()

if __name__ == "__main__":
    r = ROV()
    r._data["dearclient"]["thrusters"] = { "actives": [], "force": [], "thrusters": {} }
    r._data["dearclient"]["thrusters"]["actives"] = [1,1,1,1,1,1,1,1]
    r._data["dearclient"]["thrusters"]["force"] = [[1],[0],[0],[0],[0],[0]]
    r.run()
    # add print statement after self.update() in r.run()
