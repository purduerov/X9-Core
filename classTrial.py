import subprocess
import time

class classTrial():

	def getTemp():#need to parse to get only the number(outputs temp = x)
		x =(subprocess.Popen(['vcgencmd','measure_temp']))
		time.sleep(2)
		x.terminate()
		#return x.split('=')[1]#-----problem here, triple '
		
	def getClockRate():
		y =(subprocess.Popen(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq']))
		time.sleep(2)
		y.terminate()
		#return y		
	
	def getVolt():
		z =(subprocess.Popen(['vcgencmd','measure_volts']))
		time.sleep(2)
		z.terminate()
		#return z.split('=')[1]

	def getLoadAvg():
		avg = (subprocess.Popen(['cat', '/proc/loadavg']))	
		time.sleep(2)
		avg.terminate()
		#return avg

	def getMemUsed():
		u = (subprocess.Popen(['du', '-hs']))#, '/dev/root']))
		time.sleep(2)
		u.terminate()

	def endFunctions():
		x.terminate()
		y.terminate()
		z.terminate()
		avg.terminate()
		u.terminate()
		#return u.split('K')[0]		

	#print getTemp()
	#print getVolt()
	#print getClockRate()
	#print getLoadAvg()
	#print getMemUsed()
	getMemUsed()
