import math

def getAngle(d, angle):
	lenth = d/math.tan(angle* math.pi/180)
	return lenth
if __name__ == "__main__":
	depth = 2.4 #get the depth of ROV
	angleX = 30;
	angleY = 60;
	x = getAngle(depth, angleX)
	y = getAngle(depth, angleY)
	print("X: %d", x)
	print("Y: %d", y)

