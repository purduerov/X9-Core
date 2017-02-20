#from thrust_mapper import ThrustMapper

# Attemps to initialize the hardware thrustesr
# If it fails on init, then use the mock thrusters


def Thrusters():
    try:
        from Thrusters import Thrusters as Thrusters_Hardware
        return Thrusters_Hardware()
    except Exception as e:
        print "Failed to Initialize Hardware Thrusters"
        print "Error: %s" % e.message
        print "Using Mock Thrusters"
        from Thrusters_Mock import Thrusters as Thrusters_Mock
        return Thrusters_Mock()

def AltThrusters(*args):
    try:
        from Alt_Thrusters import Thrusters as Thrusters_Alt
        return Thrusters_Alt(*args)
    except Exception as e:
        print "Failed to Initialize Alt Thrusters"
        print "Error: %s" % e.message
        print "Using Mock Thrusters"
        from Thrusters_Mock import Thrusters as Thrusters_Mock
        return Thrusters_Mock()
