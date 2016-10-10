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
		INT_MAX = 1000 # max value for integrator

	# update the output, based on curr_val (position/angle based on sensors)
	def update(curr_val):
		# calculate error
		err = self.setpoint - curr_val;
		# calculate new error derivitive
		derivitive = err - self.prev_err
		# calculate new error integral
		self.integral = self.integral + err
		# limit the integral
		if self.integral > INT_MAX:
			self.integral = INT_MAX
		elif self.integral < -INT_MAX
			self.integral = -INT_MAX
		# calculate the new output value
		self.out = err * Kp+ derivitive * Kd + self.integral * Ki
		# update the previous error
		self.prev_err = err   

	# set a new target point, clears the integral and prev_err values
	def set_setpoint(sp):
		self.setpoint = sp
		self.integral = 0
		self.prev_err = 0

	# get the current output of the PID controller 
	def getOutput():
		return self.out
