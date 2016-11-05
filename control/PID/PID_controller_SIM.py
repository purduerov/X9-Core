import PID_controller
import random

class PID_sim:
	# define number of samples, amount of noise, PID parameters
	def __init__(self, time, noise, P, I, D):
		self.time = time
		self.noise = noise
		self.PID_DUT = PID_controller.PID_Controller(P,I,D)
		self.sensorVals = [0 for i in range(self.time)]

	# run a testcase with a certain setpoint
	def testcase(self, testpoint):
		self.PID_DUT.set_setpoint(testpoint)
		# create output file
		fname = "test{0}.csv".format(str(int(testpoint)))
		with open(fname,'w') as logFile:
			# loop over sensorval readings
			for idx, val in enumerate(self.sensorVals):
				#update pid based on current sensor value
				self.PID_DUT.update(val)
				# get updated output
				out = self.PID_DUT.getOutput()
				# update next sensor value based on current value, PID output, and noise
				if idx +1 < len(self.sensorVals):
					self.sensorVals[idx + 1] = self.sensorVals[idx] + out + random.uniform(-1,1) * self.noise
				# write time, sensor value, and output to file
				logFile.write(str(idx) + "," + str(val) + "," + str(out) + "\n")
		# print difference between setpoint and sensor at last timestep
		print("Difference at t={0}: {1}".format(self.time,testpoint-self.sensorVals[-1]))
			
# run a simple testcase
if __name__ == '__main__':
	sim = PID_sim(100,0.1,1.0,.01,.01)
	sim.testcase(100.0)
