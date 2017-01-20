import control.PID as PID
import control.Thrust_Mapping
import sensors.SensorClass

pidwrapper = PID.PID_wrap.PID()
pidwrapper.set_destination(0, 0, 0, 0, 0, 0)
desired = pidwrapper.engage_PID()
print desired
thrustmapper = Thrust_Mapping.thrust_mapper.ThrustMapper()
thrustmap = thrustmapper.generate_thrust_map(desired)
print thrustmap
