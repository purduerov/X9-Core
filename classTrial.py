import subprocess

class classTrial():

# BMAX:TODO: WARN: Would be a good idea to rewrite these so that they are started as non-blocking processes (so we don't wait for their output) and can be shut off/given ample time to complete just in the event that they, for some reason, get stuck or need a lot of processing to complete. We want our robot to be FAULT TOLERANT in all cases we can prepare for!
# To provide a good solution for what I'm asking you to do is to create a function that starts the process non-blocking. Create a function that checks if that process has completed and if so, what its output is. And a function to stop that process (so we can call it manually if we need to). In the implementation of this class, we will 'try' to read a process output (if a process exists) and print it to whatever interface we want, immediately after, we will restart the process. After this the remaining code will run and by the time it gets back to checking if the processes completed, those processes will have time to run for as long as they need. The only issue with this method is that the data retreived will be a little stale... the latency will be the period of an update loop (of the rov object) or the time interval we set to restart these processes.
# If you don't understand what I'm saying, DM me or talk to me at the next meeting.
fjsdlkj
	def getTemp():#need to parse to get only the number(outputs temp = x)
		x =(subprocess.check_output(['vcgencmd','measure_temp']))
		return x.split('=')[1]#-----problem here, triple '

	def getClockRate():
		y =(subprocess.check_output(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq']))
		return y

	def getVolt():
		z =(subprocess.check_output(['vcgencmd','measure_volts']))
		return z.split('=')[1]

	def getLoadAvg():
		avg = (subprocess.check_output(['cat', '/proc/loadavg']))
		return avg

	def getMemUsed():
		u = (subprocess.check_output(['du', '-hs']))
		return u

	print getTemp()
	print getVolt()
	print getClockRate()
	print getLoadAvg()
	print getMemUsed()
