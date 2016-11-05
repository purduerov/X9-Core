import matrices
import Vectors
import thrust_mapper


class ThrustersContainer(object):

    def __init__(self, powers, currents, voltages, enabled):
        self.powers = powers
        self.currents = currents
        self.voltages = voltages
        self.enables = enabled


class Overseer(object):

    NO_NEW_DATA = 0
    NEW_DATA = 1

    THRUST_MAX = 32767.0
    FLOATPT_TO_INT_SCALE = 10000

    def __init__(self):
        self.i = None
        self.flagNewData = Overseer.NEW_DATA
        powers = [0] * 8
        currents = [0] * 8
        voltages = [0] * 8
        enabled = [0] * 8
        self.thrusters = ThrustersContainer(powers, currents, voltages, enabled)
        self.thrustMapper = thrust_mapper.ThrustMapper()
        self.target_force = Vectors.vect6(0, 0, 0, 0, 0, 0)

    def update(self, force, pivotPos, on_off):
        """Gives new data to Overseer, and sets flagNewData to NEW_DATA"""
        self.target_force = force
        self.thrustMapper.adjustPivotPosition(pivotPos)
        self.thrustMapper.changeMapperMatrix(on_off)

        self.flagNewData = Overseer.NEW_DATA

    def checkForUpdate(self):
        """Checks if new data has been logged (flagNewData set), calculates if true
            :returns flagNewData
        """
        if self.flagNewData == Overseer.NEW_DATA:
            self.calculateAndPush()
        return self.flagNewData

    def calculateAndPush(self):
        """Calculates the required thrusts for each motor and pushes to the motors"""
        self.thrustMapper.calculateThrustMap(self.target_force)
        max = matrices.Matrices.max8(self.thrustMapper.thrust_map)
        if max > Overseer.THRUST_MAX:
            self.scaleOverflow(max)

    def scaleOverflow(self, max):
        """Scales all thrust values by the maximum overflowing thrust, keeping the same force vector"""
        if max < Overseer.THRUST_MAX:
            return

        scale = float(Overseer.THRUST_MAX) / max
        scale *= Overseer.FLOATPT_TO_INT_SCALE

        a = self.thrustMapper.thrust_map.a * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        b = self.thrustMapper.thrust_map.b * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        c = self.thrustMapper.thrust_map.c * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        d = self.thrustMapper.thrust_map.d * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        e = self.thrustMapper.thrust_map.e * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        f = self.thrustMapper.thrust_map.f * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        g = self.thrustMapper.thrust_map.g * scale / int(Overseer.FLOATPT_TO_INT_SCALE)
        h = self.thrustMapper.thrust_map.h * scale / int(Overseer.FLOATPT_TO_INT_SCALE)

        self.thrustMapper.thrust_map = Vectors.vect8(a, b, c, d, e, f, g, h)

    def doRamping(self):
        pass

    def updateFromThrusters(self):
        return self.thrustMapper.getThrustMap()
