import cv2 as cv
from matplotlib import pyplot as plt
import cv2
import numpy as np
from PIL import Image
from PIL import ImageEnhance

def computeEdgeMask(img):



    return img

# http://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html
def graphImageHist(imageIn):
    img = imageIn
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

def equalizeHist(imageIn):
    hist, bins = np.histogram(imageIn.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    return cdf[imageIn]

def claheEqualizeHist(img):
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(img)
    return cl1

def pilImageToOpenCv(pil_image):
    open_cv_image = np.array(pil_image)
    # Convert RGB to BGR
    return open_cv_image[:, :, ::-1].copy()

def pilColorConverter():
    # Need to load the color separately using the PIL library
    img = Image.open('ProcessedImages/GOPR0041.jpg').convert('RGB')
    converter = ImageEnhance.Color(img)
    img = pilImageToOpenCv(converter.enhance(r / 2))
def nothing(x):
    pass

def loop():
    # Load the image with PIL then convert to opencv
    img = cv.imread('ProcessedImages/GOPR0041.jpg')

    cv.imshow("test1", img)

    cv2.createTrackbar('cSat', 'test1', 0, 20, nothing)

    while True:
        cv.imshow("test1", img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        r = cv2.getTrackbarPos('cSat', 'test1')

    cv2.destroyAllWindows()




if __name__ == "__main__":
    img = cv.imread('ProcessedImages/GOPR0041.jpg')
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", grayImg)
    cv.imshow("Hist", equalizeHist(grayImg))
    cv.imshow("CLAHE", claheEqualizeHist(grayImg))
    cv.waitKey()