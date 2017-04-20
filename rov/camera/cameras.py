import os
import time

from camera import Camera


class Cameras(object):
    # default layout for camera
    def __init__(self, resolution='640x480', framerate=30, port_start=8080, brightness=16, contrast=32):
        self.cameras = []
        self.port_start = port_start

        self.resolution = resolution
        self.framerate = framerate
        self.brightness = brightness
        self.contrast = contrast

        self.video_devices = [dev for dev in os.listdir('/dev') if dev.startswith('video')]

        for i in range(len(self.video_devices)):
            cam = Camera(
                resolution=self.resolution,
                framerate=self.framerate,
                device='/dev/' + self.video_devices[i],
                port=self.port_start + i,
                brightness=self.brightness,
                contrast=self.contrast
            )

            self.cameras.append(cam)

        # clear previous open ones
        self.system_kill()

        self.start()

    def start(self):
        for cam in self.cameras:
            time.sleep(0.2)
            cam.start()

    def kill(self):
        for cam in self.cameras:
            cam.kill()

        self.system_kill()

    def system_kill(self):
        os.system("pgrep 'mjpg' | xargs kill -9")

    def status(self):
        return {
            cam.device: {'port': cam.port, 'status': cam.get_status()}
            for cam in self.cameras
        }

    def set_status(self, status):
        for cam in self.cameras:
            if cam.device in status:
                cam.set_status(status[cam.device])


if __name__ == "__main__":
    cameras = Cameras()
    cameras.start()

    while True:
        c_status = cameras.status()
        for c in c_status:
            print ""
            print "Name:   %s" % c
            print "Status: %s" % c_status[c]['status']
            print "Port:   %s" % c_status[c]['port']

        time.sleep(2)
