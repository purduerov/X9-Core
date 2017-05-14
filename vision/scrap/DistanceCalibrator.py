import cv2 as cv
import math
import numpy as np


DOTS_DISTANCE = .33655 #Meters

"""Module locates green dots in an image and returns the pixel
to distance ratio of the image assuming the image is being observed
from above"""

def getRatioPx_DistMeters(img):

    #Clean up the noise
    blurred =cv.medianBlur(img,7)

    #Threshold out the color we want
    colorThreshed = cv.inRange(blurred, (50,140,0), (100, 200, 10))
    gray = cv.Canny(colorThreshed, 70, 100)

    circles = cv.HoughCircles(gray, cv.cv.CV_HOUGH_GRADIENT,1,10, param1=100, param2=15, minRadius=1, maxRadius=20)
    if circles is None or len(circles[0]) != 2:
        raise RuntimeError("Calibration circles not found")

    for circle in circles[0]:
        cv.circle(img, tuple(circle[0:2]), 3, (0,255,0), thickness=1)

    #Calculate distance ratio
    return  np.linalg.norm(np.array(circles[0][0][0:2]) - np.array(circles[0][1][0:2])) / DOTS_DISTANCE, circles


"""Returns the angle relative to the top of the picture in degrees of the pool line"""
def getAnglePoolLines(img):

    blurred = cv.medianBlur(img, 7)

    #@PotentialProblem -- This tolerance may be too little
    colorThreshed = cv.inRange(blurred, (40,40,0), (140,120,40))
    gray = cv.Canny(colorThreshed, 70, 100)

    #Lines contains the [rho, theta] values for each line ordered by
    #number of votes in accumulator array (From best to worst)
    lines = cv.HoughLines(gray,1, math.pi/180,30)[0]
    if lines is None:
        raise RuntimeError("Pool lines not found")

    bestLine = lines[0]
    rhoBest = bestLine[1]
    perpLine = None

    #Find the next line that is perpendicular to the best line
    for line in lines[1::]:
        rhoCurr = line[1]

        #Find the next line that is roughly perpendicular
        if abs(abs(rhoBest-rhoCurr) - math.pi/2) < math.pi/4:
            perpLine = line
            break


    #TODO can I just return the direction of my best line or how do I determine the difference
    #TODO between the best line and the next best line
    newLines = [bestLine, perpLine]
    # CREDIT: OpenCV Docs
    for rho, theta in newLines:
        a  = np.cos(theta)
        b  = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 600 * (-b)) #TODO where is this 1000 coming from?
        y1 = int(y0 + 600 * (a))
        x2 = int(x0 - 600 * (-b))
        y2 = int(y0 - 600 * (a))

        cv.line(gray, (x1, y1), (x2, y2), 255, 1)

    cv.imshow("Angles", gray)
    cv.waitKey()

# Run calibrators test cases
if __name__ == "__main__":
    img = cv.imread('RDTestImages/testCircles.png')
    ratio, circles = getRatioPx_DistMeters(img)

    # Debug -- circle radius locator
    # for circle  in circles[0]:
    #    cv.circle(img, tuple(circle[0:2]), circle[2], (0,255,0))

    img2 = cv.imread('ProcessedImages/GOPR0033.jpg')
    print(getAnglePoolLines(img2))
