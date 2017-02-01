from BlueRobotics_Bar30 import Pressure as BlueRobotics_Bar30
from Pressure_Mock import Pressure as Pressure_Mock

# Attemps to initialize and read the Bar30 sensor.
# If it fails updating, then use the mock pressure library.

def Pressure():
    try:
        pressure = BlueRobotics_Bar30()
        # Call update so it can try writing some bytes
        # It should fail fast when not connected
        pressure.update()
        return pressure
    except Exception:
        print "Failed to Initialize BlueRobotics Bar30 Pressure Sensor"
        print "Using Mock Pressure Sensor"
        return Pressure_Mock()
