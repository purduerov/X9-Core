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
    def generate_matrix(self, lrrelation, udrelation):
        rads = math.radians(22)
        right_coe = (lrrelation * (self.radius2 * self.rot_angle2 + self.radius4 * self.rot_angle4)) - (2 * math.cos(rads))
        left_coe = (lrrelation * (self.radius1 * self.rot_angle1 + self.radius3 * self.rot_angle3)) + (2 * math.cos(rads))
        left_needed = (1 / math.cos(rads)) / ((left_coe / right_coe) * 2 + 2)
        right_needed = (left_coe / right_coe) * left_needed
        right_coe += (2 * math.cos(rads))
        left_coe -= (2 * math.cos(rads))
        right_coe /= lrrelation
        left_coe /= lrrelation
        left = 1 / math.cos(rads) / ((left_coe / right_coe) * 2 + 2)
        right = (left_coe / right_coe) * left
        rot1_1 = abs(left_needed - left) * lrrelation
        rot1_2 = abs(right_needed - right) * lrrelation
        if abs(rot1_1 - rot1_2) < 0.0000000001:
            print "rot1_1 == rot1_2"
        else:
            print "rot1_1 != rot1_2"

        upper_coe = (udrelation * (self.radius1 * self.rot_angle1 + self.radius2 * self.rot_angle2)) + (2 * math.sin(rads))
        lower_coe = (udrelation * (self.radius3 * self.rot_angle3 + self.radius4 * self.rot_angle4)) - (2 * math.sin(rads))
        upper_needed = (1 / math.sin(rads)) / ((upper_coe / lower_coe) * 2 + 2)
        lower_needed = (upper_coe / lower_coe) * upper_needed
        upper_coe -= (2 * math.sin(rads))
        lower_coe += (2 * math.sin(rads))
        upper_coe /= udrelation
        lower_coe /= udrelation
        upper = (1 / math.sin(rads)) / ((upper_coe / lower_coe) * 2 + 2)
        lower = (upper_coe / lower_coe) * upper
        rot2_1 = abs(upper_needed - upper) * udrelation
        rot2_2 = abs(lower_needed - lower) * udrelation
        if abs(rot2_1 - rot2_2) < 0.0000000001:
            print "rot2_1 == rot2_2"
        else:
            print "rot2_1 != rot2_2"
        if abs(rot1_1 - rot2_1) < 0.0000000001:
            print "rot1_1 == rot2_1"
        else:
            print "rot1_1 != rot2_1"
        print "%(left).9f\t%(right).9f\t%(upper).9f\t%(lower).9f\t%(rot1).9f\t%(rot2).9f" % \
              {'left': left, 'right': right, 'upper': upper, 'lower': lower, 'rot1': rot1_1, 'rot2': rot2_1}

maker = MatrixMaker(3, -1.5, 3, 1, -2, -1.5, -2, 1)
desired = [.5, 1, 0, 0, 0, 1]
relation1 = 1
relation2 = 1
try:
    relation1 = desired[0] / desired[5]
except ZeroDivisionError:
    relation1 = 1
try:
    relation2 = desired[1] / desired[5]
except ZeroDivisionError:
    relation2 = 1
if desired[0] == 0:
    relation1 = 1
if desired[1] == 0:
    relation2 = 1
maker.generate_matrix(relation1, relation2)
