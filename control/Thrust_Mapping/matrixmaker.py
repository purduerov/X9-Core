import math


class MatrixMaker(object):

    def __init__(self, location1x, location1y, location2x, location2y, location3x, location3y, location4x, location4y):
        self.thruster1 = [location1x, location1y]
        self.thruster2 = [location2x, location2y]
        self.thruster3 = [location3x, location3y]
        self.thruster4 = [location4x, location4y]
        self.radius1 = ((self.thruster1[0] ** 2) + (self.thruster1[1] ** 2)) ** 0.5
        self.radius2 = ((self.thruster2[0] ** 2) + (self.thruster2[1] ** 2)) ** 0.5
        self.radius3 = ((self.thruster3[0] ** 2) + (self.thruster3[1] ** 2)) ** 0.5
        self.radius4 = ((self.thruster4[0] ** 2) + (self.thruster4[1] ** 2)) ** 0.5
        self.rot_angle1 = math.sin(math.acos(abs(self.thruster1[0] / self.radius1)) + math.radians(22))
        self.rot_angle2 = math.sin(math.acos(abs(self.thruster2[0] / self.radius2)) + math.radians(22))
        self.rot_angle3 = math.sin(math.acos(abs(self.thruster3[0] / self.radius3)) + math.radians(22))
        self.rot_angle4 = math.sin((math.radians(90) - math.acos(abs(self.thruster4[0] / self.radius4))) + math.radians(22))

    # add proportionality constant to allow for different values (need one for left/right and up/down?)
    def generate_matrix(self):
        rads = math.radians(22)
        right_coe = (self.radius2 * self.rot_angle2 + self.radius4 * self.rot_angle4) - (2 * math.cos(rads))
        left_coe = (self.radius1 * self.rot_angle1 + self.radius3 * self.rot_angle3) + (2 * math.cos(rads))
        left_needed = (1 / math.cos(rads)) / ((left_coe / right_coe) * 2 + 2)
        right_needed = (left_coe / right_coe) * left_needed
        right_coe += (2 * math.cos(rads))
        left_coe -= (2 * math.cos(rads))
        left = 1 / math.cos(rads) / ((left_coe / right_coe) * 2 + 2)
        right = (left_coe / right_coe) * left
        rot1_1 = abs(left_needed - left)
        rot1_2 = abs(right_needed - right)
        if abs(rot1_1 - rot1_2) < 0.0000000001:
            print "rot1_1 == rot1_2"
        else:
            print "rot1_1 != rot1_2"

        upper_coe = (self.radius1 * self.rot_angle1 + self.radius2 * self.rot_angle2) + (2 * math.sin(rads))
        lower_coe = (self.radius3 * self.rot_angle3 + self.radius4 * self.rot_angle4) - (2 * math.sin(rads))
        upper_needed = (1 / math.sin(rads)) / ((upper_coe / lower_coe) * 2 + 2)
        lower_needed = (upper_coe / lower_coe) * upper_needed
        upper_coe -= (2 * math.sin(rads))
        lower_coe += (2 * math.sin(rads))
        upper = (1 / math.sin(rads)) / ((upper_coe / lower_coe) * 2 + 2)
        lower = (upper_coe / lower_coe) * upper
        rot2_1 = abs(upper_needed - upper)
        rot2_2 = abs(lower_needed - lower)
        if abs(rot2_1 - rot2_2) < 0.0000000001:
            print "rot2_1 == rot2_2"
        else:
            print "rot2_1 != rot2_2"
        if abs(rot1_1 - rot2_1) < 0.0000000001:
            print "rot1_1 == rot2_1"
        else:
            print "rot1_1 != rot2_1"
        print "%(left)f\t%(right)f\t%(upper)f\t%(lower)f\t%(rot1)f\t%(rot2)f" % {'left': left, 'right': right,
                                                                                 'upper': upper, 'lower': lower,
                                                                                 'rot1': rot1_1, 'rot2': rot2_1}

maker = MatrixMaker(1, -2, 1, 1, -1, -2, -1, 1)
maker.generate_matrix()
