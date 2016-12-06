from time import time, sleep


class ROV(object):

    def __init__(self):
        self.data = {}
        self.last_update = 0

    def update(self):
        print "Update! %.5f" % (time() - self.last_update)

        self.last_update = time()

    def run(self):
        while True:
            while time() - self.last_update < 0.01:
                sleep(0.0001)

            self.update()

if __name__ == "__main__":
    r = ROV()
    r.run()
