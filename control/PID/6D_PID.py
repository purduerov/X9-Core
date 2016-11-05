class PID_Controller:
	#constructor sets PID coeffs, initialize vars
	def __init__(self,P=0.1,I=0.01,D=0.0):
		self.Kp = P
		self.Ki = I
		self.Kd = D
		self.prev_err = 0 # the previous value of the error
		self.integral = 0 # integral value
		self.out = 0 # output of controller
		self.setpoint  = 0 # the desired point
		self.INT_MAX = 1000 # max value for integrator
