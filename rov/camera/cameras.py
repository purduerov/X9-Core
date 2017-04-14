import os
from camera import Camera

class Cameras:
    # default layout for camera
    def __init__(self, resolution='1024x768', framerate=30, port_start=8080, brightness=16, contrast=32):
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

            cam.start()

            self.cameras.append(cam)

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
    import time

    cameras = Cameras()
    time.sleep(2)
    print cameras.status()

