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


class ROV(object):

    def __init__(self, lock, data):

        self._data_lock = lock
        self._data = data
        self.dearclient = {"thrusters": {}}

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
                #print "flask"
                #print self._data['dearflask']["thrusters"]#["t7"]
                #print "client"
                #print self._data['dearclient']["thrusters"]
                t = ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"]
                f = ["x", "y", "z", "roll", "pitch", "yaw"]
                print "in update"
                #print self._data['dearflask']
                #for x in self._data['dearflask']:
                #    print x
                print 'Thruster Data:'
                print self._data['dearflask'][u'thrusters']
                print 'Thruster 6:'
                print self._data['dearflask'][u'thrusters'][u't6']
                print 'Thruster 6 active:'
                print self._data['dearflask']['thrusters']['t6']['active']

                print 'Looping over thrusters for active list'
                for x in t:
                    #print "LOOK AT ME DAMMIT I'M PRETTY"
                    #print self._data['dearflask']["thrusters"][t+tval]
                    #print "active"
                    print x
                    #print t[u'active']
                    actives.append(self._data['dearflask'][u'thrusters'][x]['active'])
                    #print t
                    #print t["active"]
                    #actives.append(self._data['dearflask']['thrusters'][t+tval]["active"])
                for z in f:
                    force.append(self._data['dearflask']['force'][z] * .35)
                print "finished actives"
                print "Actives:"
                print actives
                #force = self._data['dearflask']['force']
                print "Force:"
                print force
                print 0.35 * np.array(force)
                #thrust = self.mapper.generate_thrust_map(np.array(actives), 0.35 * np.array(force))
                #thrust = list(np.asarray(thrust)[0])
                #self.thrusters.push_pi_motors(thrust, actives)
                self.thrusters.temp_move(force, actives)
                print "Thrust:"
                print thrust
                print self._data['dearflask']['thrusters']['t6']

                #self._data['dearclient']["thrusters"]["thrusters"] = self.thrusters.get_data()
                self.dearclient["thrusters"] = self.thrusters.get_data()

            except TypeError as err:
                print "Here"
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
