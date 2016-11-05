from PIL import Image
class laser_rangefinder(object):
    """ 
    Determintes distance to object based on camera and laser points
    """
    def __init__(self):
        """
        Init the laser laser_rangefinder
        """
        self.FOCAL_LENGTH = 357 # maybe?
        self.LASER_SPACING = 0.1016 # we'll have to measure this in real life
        self.distance = 0.0
        self._redThreshold = 180

    def _dot_dist(self, img):
        im = Image.open(img)
        r,g,b = im.split()
        width, height = g.size
        xStart = 330
        xMid = 380
        xEnd = 430
        yStart = 305
        yEnd = 330


        left = xMid
        right = xStart
        good = 0
        for i in range(yStart,yEnd):
            for j in range(xStart,xMid):
                x = r.getpixel((j,i))
                if x > self._redThreshold:
                    good = 1
                    if j < left:
                        left = j
                    if j > right:
                        right = j
                else:
                    r.putpixel((j,i),0)
        p1 = (right + left) / 2
        if not good:
            print("bad")
        left = xEnd
        right = xMid
        for i in range(yStart,yEnd):
            for j in range(xMid,xEnd):
                x = g.getpixel((j,i))
                if x > self._redThreshold:
                    if j < left:
                        left = j
                    if j > right:
                        right = j
                else:
                    r.putpixel((j,i),0)
        r.save("testout.jpg")
        p2 = (right + left) / 2
        return p2 - p1


    def _calc_distance(self,imageFile):
        """
        get the distance between lasers in pixels
        compute distance based on measured focal length
        """
        pixel_dist = self._dot_dist(imageFile)
        self.distance =  ((self.FOCAL_LENGTH * self.LASER_SPACING) / pixel_dist)
        print(pixel_dist)

    def get_distance(self):
        """
        returns the distance to the position of the lasers
        """
        # this file will be whatever we tell the mjpg streamer to use
        self._calc_distance("laserImages/12feet1.jpg")
        return self.distance

if __name__ == '__main__':
    DUT = laser_rangefinder()
    print(DUT.get_distance())
