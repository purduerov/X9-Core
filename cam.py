import subprocess
import requests
import os

class Camera:
	
	def __init__(self, resolution = '1024x768', framerate = 30, device = '/dev/video0', port = 8080, brightness = 16, contrast = 32):
		
		self.switch = None 
		self.r = resolution 
		self.f = framerate
		self.d = device
		self.p = port
		self.b = brightness
		self.c = contrast
		self.inp = 'input_uvc.so -r ' + self.r + ' -f ' + str(self.f) + ' -d ' + self.d + ' -br ' + str(self.b) + ' -co ' + str(self.c)
		self.out = 'output_http.so -w /usr/local/www -p ' + str(self.p)
	
	def on(self):
		self.switch = subprocess.Popen(['mjpg_streamer', '-i', self.inp, '-o', self.out])

	def off(self):
		self.switch.kill()
	
	def saveImage(self, fil = 'image.jpg'):
		r = requests.get('http://localhost:' + str(self.p) + '/?action=snapshot', stream=True)
		with open(fil, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)

class start:
	
	def __init__(self):
		self.devs = cameraDevices = []
		self.camNum = []
		temp = 97
		for filename in os.listdir("/dev"):
			if filename.startswith('video'):
				self.devs.append('/dev/' + filename)
				self.camNum.append('97')
				temp = temp + 1

		for x in range(0, len(self.devs)):
			self.camNum[x] = Camera(device = self.devs[x], port = 8080 + x)
			self.camNum[x].on()
	def destroy(self):
		for y in range(0, len(self.devs)):
			self.camNum[y].off()
