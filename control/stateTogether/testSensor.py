dataset = open("output.txt",'r')

class testSensor(object):
    def __init__(self):
        self.data1 = ""
        self.data2 = ""

    def getData(self):
        data1 = dataset.readline()
imu = testSensor ()
while(1):
    print  dataset.readline()
