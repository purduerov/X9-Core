import math
arrayLength = 1000
max = 255
numPulse = 5
freq = 8000

def genArray(length):
	x = 0;

	toPrint = str(math.floor(math.sin(x*2*math.pi/100)*max/2)+max/2)
	while (x<(length-1)):
		x = x + 1
		if(x < 500):
			sample = math.floor(math.sin(x*2*math.pi/100)*max/2)+max/2
		else:
			sample = max/2
		toPrint = toPrint + ','
		toPrint = toPrint + str(sample)
	toPrint = toPrint + '};'
	return toPrint


array = "int StandardSignal[SignalSetupLength] = {"
with open('ROV_sonar.ino','r') as file:
	data = file.readlines()

array = array + genArray(arrayLength) + '\n'
data[25] = array
print array
with open('ROV_sonar.ino','w') as file:
	file.writelines(data)

