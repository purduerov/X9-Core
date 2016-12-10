import subprocess
import time

class Camera:

	def __init__(self, resolution, framerate, device, port):

		self.res = resolution 
		self.fr = framerate
		self.switch = None 
		self.d = device
		self.port = port
		self.input_str = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/input_uvc.so -r ' + self.res + ' -f ' + str(self.fr) + ' -d ' + self.d
		self.output_str = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/output_http.so -w /usr/local/www -p ' + str(self.port)

	def onCamera(self):
		self.switch = subprocess.Popen(['mjpg_streamer', '-i', self.input_str, '-o', self.output_str])

	def offCamera(self):
		self.switch.kill()
