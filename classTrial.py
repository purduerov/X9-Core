import subprocess
import time

class RasPiStats():

        x = None
        y = None
        z = None
        avg = None
        u = None

	def startTemp():#need to parse to get only the number(outputs temp = x)
		x =(subprocess.Popen(['vcgencmd','measure_temp']))
		#return x.split('=')[1]#-----problem here, triple '

	def startClockRate():
		y =(subprocess.Popen(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq']))
		#return y

	def startVolt():
		z =(subprocess.Popen(['vcgencmd','measure_volts']))
		#return z.split('=')[1]

	def startLoadAvg():
		avg = (subprocess.Popen(['cat', '/proc/loadavg']))
		#return avg

	def startMemUsed():
		u = (subprocess.Popen(['du', '-hs']))#, '/dev/root']))

        def getTemp():
            if x != None and x.poll()==True:
                # TODO: if stdout is not reporting output, change popen constructor argument stdout=PIPE //to do this put it outside array brackets but within parenthesis([~~~~], PIPE) 
                for line in x.stdout:
                    print(line)
                x = None
                return True
            return False


        def getClockRate():
            if y != None and y.poll()==True:
                for line in y.stdout:
                    print(line) #save text somewhere else

        def getVolt():
            if z != None and z.poll()==True:
                for line in z.stdout:
                    print(line)
        
        def getLoadAvg():
            if avg != None and avg.poll()==True:
                for line in avg.stdout:
                    print(line)

        def getMemUsed():
            if u != None and u.poll()==True:
                for line in u.stdout:
                    print(line)

	def endFunctions(id=0):
            if id==0 and (x != None and y != None and z != None and avg != None and u != None):
                # TODO: change terminate to kill
                x.terminate()
                y.terminate()
                z.terminate()
                avg.terminate()
                u.terminate()
            if id==1:
                x.terminate()
            if id==2:
                y.terminate()
            if id==3:
                z.terminate()
            if id==4:
                avg.terminate()
            if id==5:
                u.terminate()

#print getTemp()
#print getVolt()
#print getClockRate()
#print getLoadAvg()
#print getMemUsed()
#getMemUsed()

if __name__ == '__main__': #if the name of the class is the same as the one being called, run this code
    test = RasPiStats()

    test.startTemp()

    while test.getTemp() != False:
        pass
    #test.endFunctions(0)
