class PID_Controller(object):
	""" PID Controller Class
	"""
	def __init__(self, P=0.1 ,I=0.01 ,D=0.0):
		"""
		Initialize the PID controller with the given P, I, D values
		"""
		self.Kp = P
		self.Ki = I
		self.Kd = D
		self.prev_err = 0 # the previous value of the error
		self.integral = 0 # integral value
		self.out = 0 # output of controller
		self.setpoint  = 0 # the desired point
		self.INT_MAX = 1000 # max value for integrator

	def update(self, curr_val):
		"""
	    update the output, based on curr_val (position/angle based on sensors)
		"""
		# calculate error
		err = self.setpoint - curr_val;
		# calculate new error derivitive
		derivitive = err - self.prev_err
		# calculate new error integral
		self.integral = self.integral + err
		# limit the integral
		if self.integral > self.INT_MAX:
			self.integral = self.INT_MAX
		elif self.integral < -self.INT_MAX:
			self.integral = -self.INT_MAX
		# calculate the new output value
		self.out = err * self.Kp+ derivitive * self.Kd + self.integral * self.Ki
		# update the previous error
		self.prev_err = err

	def set_setpoint(self, sp):
		"""
		set a new target point, clears the integral and prev_err values
		"""
		self.setpoint = sp
		self.integral = 0
		self.prev_err = 0

	def getOutput(self):
		"""
		# get the current output of the PID controller
		"""
		return self.out
