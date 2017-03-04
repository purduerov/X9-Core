from Adafruit_PCA9685 import PCA9685
import time, pprint     # For Testing code
import numpy            # For Compliance with thrust_mapping outputs

# using PCA9685 object:
# functions:
# set all pwm power with pwm.set_all_pwm(end_low, end_high)
# set pwm power with pwm.set_pwm(thrusterid, end_low, end_high)
#   To set PWM power % (-100% to 100%) w/ end_low and end_high: know that the
#   values don't matter, just the difference between them. The zero power
#   setting is 1.5ms high out of a 20ms period, which is 50Hz. The max
#   documented range for these T200 thrusters is 1.1ms to 1.9ms high.
#   The values we can use in this function lets us specify values between 0
#   and 4096, which are what we enter in end_low and end_high. So to get 1.5ms
#   high in a 20ms period, we set end_low=0 and end_high=310, for 4096 units
#   out of 20ms, 4096/20 = 204.8 units/ms. If we want diff for 1.5ms, we set
#   204 units/ms * 1.5ms = 307 units. This is the theoretical difference we
#   need, however under experimentation using logic analyzers, to achieve real
#   1.5 ms the difference should really be 310. So to set this 0% power, we
#   can call pwm.set_pwm(0, 0, 310) or pwm.set_pwm(0, 1024, 1334), there should
#   be no physical difference.


#   TORNADO THRUSTER MAPPING DOCUMENTATION:
#
# According to Jakob's Thrustmapping Matlab that Jason supplied me, my
# interpreted positions of the thrusters by location within matrix are:
#   [[front_left_horiz],
#    [front_right_horiz],
#    [back_left_horiz],
#    [back_right_horiz],
#    [front_left_vert],
#    [front_right_vert],
#    [back_left_vert],
#    [back_right_vert]]
# So my guess for what the associated pins and power distribution box labels
# for these positions in order should be:
#   [[6, H1],
#    [1, H2],
#    [4, H3],
#    [3, H4],
#    [5, V5],
#    [12, V6],
#    [8, V7],
#    [9, V9]]

class Thrusters:

    NUM_THRUSTERS = 8

    ZERO_POWER = 310
    POS_MAX_POWER = 227
    NEG_MAX_POWER = 393

    def __init__(self):
        self.t0 = Thruster()
        self.t1 = Thruster()
        self.t2 = Thruster()
        self.t3 = Thruster()
        self.t4 = Thruster()
        self.t5 = Thruster()
        self.t6 = Thruster()
        self.t7 = Thruster()
        self.thrusters = [self.t0, self.t1, self.t2, self.t3, self.t4, self.t5, self.t6, self.t7]

        # Public segment:
        self._data = { "t0": self.t0.data, "t1": self.t1.data, "t2": self.t2.data, "t3": self.t3.data, "t4": self.t4.data, "t5": self.t5.data, "t6": self.t6.data, "t7": self.t7.data }

        # Pi -> I2C-to-PWM variables:
        #   I2C-to-PWM Pins
        self.pins = [6, 1, 4, 3, 5, 12, 8, 9]
        #   I2C-to-PWM chip class:
        pwm = PCA9685()
        # pwm frequency should be 50Hz, but with chip inaccuracy, setting 50 is actually 53, so we set it to 47 to offset.
        pwm.set_pwm_freq(47)
        # thrusters must be set to 0 before they can be set to any other value.
        pwm.set_all_pwm(0, self.ZERO_POWER)


        # Pi -> Coprocessor variables:

    # BMAX:TODO: Implement pushing motors to coprocessor, which will then push motors to i2c to pwm chip.
    def push_coprocessor_motors(self):
        pass

    def push_pi_motors(self, powers, actives):

        # Update thruster data
        for t in range(0, self.NUM_THRUSTERS):
            self.thrusters[t].setActive(int(actives[t]))
            self.thrusters[t].setTarget(float(powers[t]))

        # Ramp the power from current to reach target
        _ramp()

        # Push calculated, ramped power to thrusters
        for t in range(0, self.NUM_THRUSTERS):

            # if inactive thruster:
            if (self.thrusters[t].getActive() == 0):
                self.thrusters[t].setPWMActual(self.ZERO_POWER)
                self.thrusters[t].setCurrent(0)

                pwm.set_pwm(self.pins[t], 0, thrusters[t].getPWMActual)
                continue

            # Otherwise active:

            # IF NOT RAMPED, direct power conversion:
            self.thrusters[t].setPWMActual(self.ZERO_POWER + int(self.thrusters[t].getTarget() * (self.POS_MAX_POWER - self.ZERO_POWER)))
            self.thrusters[t].setCurrent(self.thrusters[t].getTarget())

            pwm.set_pwm(self.pins[t], 0, self.thrusters[t].getPWMActual())

    def stop(self):
        for t in range(0, self.NUM_THRUSTERS):
            self.thrusters[t].setPWMActual(self.ZERO_POWER)
            self.thrusters[t].setCurrent(0)
            pwm.set_pwm(self.pins[t], 0, self.ZERO_POWER)
        print("EMERGENCY STOP CALLED: Thrusters have been stopped!")
        pwm.set_all_pwm(0, self.ZERO_POWER)

    def _ramp(self):
		for t in range(0, self.NUM_THRUSTERS):
			
			if (self.thrusters[t].getActive() == 1):
				
				ramp = self.thrusters[t].getCurrent()
				ramp_actual = self.thrusters[t].getPWMActual()
				
				ramp_percent_diff = 5 #(% from 0 to +/- 100)
				ramp_actual_diff = ((NEG_MAX_POWER - POS_MAX_POWER) / 2) * 0.05 #equal to 4.15 (5% of zero to max pos/neg)
				
				#percentage incriment/decrement (-100 to 100)
				while (self.thrusters[t].getTarget != ramp):
					if (self.thrusters[t].getTarget > ramp):
						if (self.thrusters[t].getTarget - ramp > ramp_percent_diff - 1):
							ramp = ramp + ramp_percent_diff
						else:
							ramp = ramp + 1
					if (self.thrusters[t].getTarget < ramp):
						if (ramp - self.thrusters[t].getTarget > ramp_percent_diff - 1):
							ramp = ramp - ramp_percent_diff
						else:
							ramp = ramp - 1
					
					self.thrusters[t].setCurrent(self, ramp)
				
				#value increment/decrement (393 to 227)	
				while (self.thrusters[t].getTargetActual != ramp_actual):
					if (self.thrusters[t].getTargetActual > ramp_actual):
						if (self.thrusters[t].getTargetActual - ramp_actual > ramp_actual_diff - 1):
							ramp_actual = ramp_actual + ramp_actual_diff
						else:
							ramp_actual = ramp_actual + 1
					if (self.thrusters[t].getTargetActual < ramp_actual):
						if (ramp_actual - self.thrusters[t].getTargetActual > ramp_actual_diff - 1):
							ramp_actual = ramp_actual - ramp_actual_diff
						else:
							ramp_actual = ramp_actual - 1
							
					self.thrusters[t].setPWMActual(self, ramp_actual)
					
					
				if (self.thrusters[t].getTarget == ramp):
					self.thrusters[t].setCurrent(self.thrusters[t].getTarget())
					self.thrusters[t].setPWMActual(self.thrusters[t].getTargetActual())
			
			else:
				self.thrusters[t].stop()
			
			
		
		

    def get_data(self):
        return self._data


class Thruster:
    def __init__(self):
        self.data = {
            "active": 0,        # int, 0 is inactive, 1 is active.
            "target": 0.0,      # float, percentage (< 1) power thrustmapping gives Thrusters through push_? methods.
            "current": 0.0,     # float, percentage (< 1) power of the actually being applied via pwm_actual. Used by _ramp.
            "pwm_actual": 0 }   # int, actual converted power from NEG_MAX_POWER to POS_MAX_POWER, representing current power percentage

    def setActive(self, value):
        self.data["active"] = value

    def setTarget(self, value):
        self.data["target"] = value

    def setCurrent(self, value):
        self.data["current"] = value

    def setPWMActual(self, value):
        self.data["pwm_actual"] = value

    def getActive(self):
        return self.data["active"]

    def getTarget(self):
        return self.data["target"]
	
	def getTargetActual(self):
		#convert getTarget % value to actual value 
        return self.data["target_actual"]

    def getCurrent(self):
        return self.data["current"]

    def getPWMActual(self):
        return self.data["pwm_actual"]



# TEST:
if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    ts = Thrusters()

    print("MOTORS TEST from thrusters.py:")
    print("===========================================")

    print("Turn all motors on 20% forward in sequence:")
    print("t0:")
    ts.push_pi_motors([.2,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t1:")
    ts.push_pi_motors([0,.2,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t2:")
    ts.push_pi_motors([0,0,.2,0,0,0,0,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t3:")
    ts.push_pi_motors([0,0,0,.2,0,0,0,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t4:")
    ts.push_pi_motors([0,0,0,0,.2,0,0,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t5:")
    ts.push_pi_motors([0,0,0,0,0,.2,0,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t6:")
    ts.push_pi_motors([0,0,0,0,0,0,.2,0], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("t7:")
    ts.push_pi_motors([0,0,0,0,0,0,0,.2], [1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    raw_input("Press Enter to continue...")
    ts.push_pi_motors([0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1])

    print("Sequence test over...!")

    print("===========================================")

    print("Next, testing thruster activity settings")
    ts.push_pi_motors([.2,.2,.2,.2,.2,.2,.2,.2], [0,0,0,0,0,0,0,0])
    pp.pprint(ts.get_data())
    print("CHECK: ALL MOTORS SHOULD BE STOPPED!")
    raw_input("Press Enter after CHECKING THRUSTER ACTIVITY...")

    print("===========================================")

    print("Next, testing emergency stop method")
    print("Starting motors at 20% reverse.")
    ts.push_pi_motors([-.2,-.2,-.2,-.2,-.2,-.2,-.2,-.2],[1,1,1,1,1,1,1,1])
    pp.pprint(ts.get_data())
    time.sleep(3)
    print("Stopping motors in:")
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
    ts.stop()
    pp.pprint(ts.get_data())
    print("STOPPED!")
    raw_input("Press Enter to end Test.")

