import subprocess

class Camera:

	# default layout for camera, allows only one camera to function at any point in time unless changed in changeSet method
	def __init__(self, resolution='WXGA', framerate=30, device='/dev/video0', port='8080'):

		self.switch = None
		self.r = resolution
		self.f = framerate
		self.d = device
		self.p = port
		self.inp = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/input_uvc.so -r ' + self.r + ' -f ' + str(self.f) + ' -d ' + self.d
		self.out = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/output_http.so -w /usr/local/www -p ' + str(self.p)

	# allows the resolution, framerate, device and port to be changed, also the only way to have multiple cameras working at once
	# resolution is put in the format of a string: "VGA" - 640x480, "PAL" - 768x576, "SVGA" - 800x600, "WXGA" - 1280x720
	# framerate shouldn't be changed: keep at 30, allows for a good image while reserving valuable processing power for other devices
	# device is formatted as a string: /dev/videoNUM where NUM is the number for the order in which camera is plugged in, starting at 0
	# port is the web port where you want to output image to: change as needed
	def changeSet(self, resolution, framerate, device, port):

		self.r = resolution
		self.f = framerate
		self.d = device
		self.p = port
		self.inp = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/input_uvc.so -r ' + self.r + ' -f ' + str(self.f) + ' -d ' + self.d
		self.out = '/home/pi/mjpg-streamer/mjpg-streamer-experimental/output_http.so -w /usr/local/www -p ' + str(self.p)

	# open video feed for an instance of Camera
	def on(self):
		self.switch = subprocess.Popen(['mjpg_streamer', '-i', self.inp, '-o', self.out])

	# closes video feed for an instance of Camera: each instance of Camera must be killed using this method
	def off(self):
		self.switch.kill()

