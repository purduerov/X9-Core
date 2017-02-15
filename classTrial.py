import subprocess
import time

#class RasPiStats():

x = None
y = None
z = None
avg = None
u = None

class RasPiStats():
        
        def __init__(self):
            pass

        def startTemp(self):#need to parse to get only the number(outputs temp = x)
            x =(subprocess.Popen(['vcgencmd','measure_temp']))
		#returM-}                     Indent the current linen x.split('=')[1]#-----problem here, triple '

	def startClockRate(self) :
            y =(subprocess.Popen(['cat','/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq']))
		#return y

        def startVolt(self):
            z =(subprocess.Popen(['vcgencmd','measure_volts']))
		#return z.split('=')[1]

        def startLoadAvg(self):
            avg = (subprocess.Popen(['cat', '/proc/loadavg']))
		#return avg

        def startMemUsed(self):
	    u = (subprocess.Popen(['du', '-hs']))#, '/dev/root']))
            u = u.split(' ')[1]


        def getTemp(self):
            if x != None and x.poll()==True:
                # TODO: if stdout is not reporting output, change popen constructor argument stdout=PIPE //to do this put it outside array brackets but within parenthesis([~~~~], PIPE) 
                for line in x.stdout:
                    print(line)
               
               #return True
            #return False

        def getClockRate(self):
            if y != None and y.poll()==True:
                for line in y.stdout:
                    print(line) #save text somewhere else

        def getVolt(self):
            if z != None and z.poll()==True:
                for line in z.stdout:
                    print(line)
        
        def getLoadAvg(self):
            if avg != None and avg.poll()==True:
                for line in avg.stdout:
                    print(line)

        def getMemUsed(self):
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

def main():
    test = RasPiStats()

    test.startTemp()
    test.getTemp()

    test.startMemUsed()
    test.getMemUsed()

    test.startTemp()
    test.getTemp()

    test.startVolt()
    test.getVolt()

    test.startClockRate()
    test.getClockRate()
    

if __name__ == '__main__':main() #if the name of the class is the same as the one being called, run this code
    
   #def main():

        #test = RasPiStats()

        #test.startTemp()
	
	#print 
        #while test.getTemp() != False:
            #pass
            #test.endFunctions(0)
