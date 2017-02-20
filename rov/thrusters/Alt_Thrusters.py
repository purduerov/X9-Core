from Adafruit_PCA9685 import PCA9685


class Thrusters(object):
    def __init__(self, active, pin_layout):
        self.active = active
        self.pin_layout = pin_layout

        self.NUM_THRUSTERS = 8

        self.ZERO_POWER = 310
        self.POS_MAX_POWER = 393
        self.NEG_MAX_POWER = 227

        self.pwm = PCA9685()
        self.pwm.set_pwm_freq(47)
        # thrusters must be set to 0 before they can be set to any other value.
        self.pwm.set_all_pwm(0, self.ZERO_POWER)

    def range_map(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return int(round(rightMin + (valueScaled * rightSpan)))

    def toPWM(self, val):
        if val > 1.0:
            return self.POS_MAX_POWER
        elif val < -1.0:
            return self.NEG_MAX_POWER
        else:
            return self.range_map(val, -1.0, 1.0, self.NEG_MAX_POWER, self.POS_MAX_POWER)


    def calculate(self, gamepad):
        #Calculate Thruster Values

        #Y (Ascend and descend)
        velY = (gamepad['buttons']['rt']['val'] - gamepad['buttons']['lt']['val'])

        #X (Strafe left and right)
        velX = (gamepad['buttons']['rb']['val'] - gamepad['buttons']['lb']['val'])

        #Z (forward and backword)
        velZ = gamepad['axes']['left']['y']

        #Yaw (rotate clockwise and counter-clockwise)
        yaw = gamepad['axes']['left']['x'] * -1

        #Pitch (rotate forward and backward)
        pitch = gamepad['axes']['right']['y']

        #Roll (rotate left to right)
        roll = gamepad['axes']['right']['x']

        # velY = velY * 0.5;
        # velX = velX * 0.5;
        # velZ = velZ * 0.5;

        # yaw = yaw * 0.15;
        # pitch = pitch * 0.4;
        # roll = roll * 0.4;

        horizontalThrusters = [0,0,0,0]
        verticalThrusters = [0,0,0,0]

        horizontalThrusters[0] += velX;
        horizontalThrusters[1] -= velX;
        horizontalThrusters[2] += velX;
        horizontalThrusters[3] -= velX;

        verticalThrusters[0] += velY;
        verticalThrusters[1] += velY;
        verticalThrusters[2] += velY;
        verticalThrusters[3] += velY;

        horizontalThrusters[0] += velZ;
        horizontalThrusters[1] += velZ;
        horizontalThrusters[2] -= velZ;
        horizontalThrusters[3] -= velZ;

        verticalThrusters[0] += pitch;
        verticalThrusters[1] += pitch;
        verticalThrusters[2] -= pitch;
        verticalThrusters[3] -= pitch;

        horizontalThrusters[0] -= yaw;
        horizontalThrusters[1] += yaw;
        horizontalThrusters[2] += yaw;
        horizontalThrusters[3] -= yaw;

        verticalThrusters[0] += roll;
        verticalThrusters[1] -= roll;
        verticalThrusters[2] += roll;
        verticalThrusters[3] -= roll;

        horizontalThrusters = self.normalize(horizontalThrusters)
        verticalThrusters = self.normalize(verticalThrusters)

        return horizontalThrusters + verticalThrusters

    def normalize(self, values):
        max_val = max([abs(x) for x in values])

        if max_val > 1.0:
            values = [x/max_val for x in values]

        return values

    def set(self, values):

        pwm_vals = [self.toPWM(x) for x in values]

        for i in range(0, self.NUM_THRUSTERS):
            if self.active[i]:
                self.pwm.set_pwm(self.pin_layout[i], 0, pwm_vals[i])
            else:
                self.pwm.set_pwm(self.pin_layout[i], 0, self.ZERO_POWER)

    def calculate_and_set(self, gamepad):
        thruster_vals = self.calculate(gamepad)
        self.set(thruster_vals)
        return [self.toPWM(x) for x in thruster_vals]
        #return thruster_vals
