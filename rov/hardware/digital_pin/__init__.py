def DigitalPin(*args, **kwargs):
    try:
        from DigitalPin import DigitalPin as DigitalPin
        return DigitalPin(*args, **kwargs)
    except Exception as e:
        print "Failed to Initialize DigitalPin"
        print "Error: %s" % e.message
        print "Using Mock Servo"
        from DigitalPin_Mock import DigitalPin as DigitalPin_Mock
        return DigitalPin_Mock()
