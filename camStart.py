from camera import Camera
import os
import time

cameraDevices = []
cam = []
temp = 97;
for filename in os.listdir("/dev"):
	if filename.startswith('video'):
		cameraDevices.append('/dev/' + filename)
		cam.append('97')
		temp = temp + 1

for x in range(0, len(cameraDevices)):
	cam[x] = Camera(device = cameraDevices[x], port = 8080 + x)
	cam[x].on()

time.sleep(600)

for y in range(0, len(cameraDevices)):
	cam[y].off()
