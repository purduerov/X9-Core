arrayLength = 5000
def genArray(length):
	x = 0;
	toPrint = str(x)

	while (x<(length-1)):
		x = x + 1
		toPrint = toPrint + ','
		toPrint = toPrint + str(x)
	toPrint = toPrint + '};'
	return toPrint


array = "int StandardSignal[SignalSetupLength] = {"
with open('ROV_sonar.ino','r') as file:
	data = file.readlines()

array = array + genArray(arrayLength) + '\n'
data[20] = array
print array
with open('ROV_sonar.ino','w') as file:
	file.writelines(data)

