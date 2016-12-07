import subprocess

class classTrial():

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
