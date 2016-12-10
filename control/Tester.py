import PID
import Thrust_Mapping
import Adafruit_BNO055
import SensorClass

pidwrapper = PID.PID_wrap.PID()
pidwrapper.set_destination(0, 0, 0, 0, 0, 0)
desired = pidwrapper.engage_PID()
print desired
thrustmapper = Thrust_Mapping.thrust_mapper.ThrustMapper()
thrustmap = thrustmapper.generate_thrust_map(desired)
print thrustmap
