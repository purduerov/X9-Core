import PID_controller
import random

class PID_sim:

	def __init__(self, time, noise, P, I, D):
		self.time = time
		self.noise = noise
		self.PID_DUT = PID_controller.PID_Controller(P,I,D)
		self.sensorVals = [0 for i in range(self.time)]

	def testcase(self, testpoint):
		self.PID_DUT.set_setpoint(testpoint)

		with open("test.csv",'w') as logFile:
			for idx, val in enumerate(self.sensorVals):
				self.PID_DUT.update(val)
				out = self.PID_DUT.getOutput()
				if idx +1 < len(self.sensorVals):
					self.sensorVals[idx + 1] = self.sensorVals[idx] + out + random.uniform(-1,1) * self.noise
				print(out)
				logFile.write(str(idx) + "," + str(val) + "," + str(out) + "\n")

		print("Difference at t={0}: {1}".format(self.time,testpoint-self.sensorVals[-1]))
			

if __name__ == '__main__':
	sim = PID_sim(100,0.1,.5,.01,.01)
	sim.testcase(3.0)
