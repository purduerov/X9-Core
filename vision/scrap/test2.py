import numpy as np
import cv2
import time



def dilateErode(img,size=10):
    kernel = np.ones((size,size),np.uint8)
    return cv2.erode(cv2.dilate(img,kernel),kernel)

def dilateErodeX(img,times=10,size=10):
    kernel = np.ones((size,size),np.uint8)
    for i in range(0,times):
        img = cv2.dilate(img,kernel)
    for i in range(0,times):
        img = cv2.erode(img,kernel)
    return img

def erodeDilateX(img, times =1, size=5):
    kernel = np.ones((size, size), np.uint8)
    for i in range(0, times):
        img = cv2.erode(img, kernel)
    for i in range(0, times):
        img = cv2.dilate(img, kernel)
    return img


def removePoolsLines(image):
    sharpKernel = np.array([[1, 1, 1],[1, -6, 1], [1,1,1]])
    img = cv2.filter2D(cv2.blur(image,(4,4)),-1,sharpKernel)
    ret, mask = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    img2 = cv2.subtract(image,cv2.bitwise_not(mask))
    img = cv2.dilate(img,np.ones((4,10),np.uint8))
    mean,std = cv2.meanStdDev(img)
    ret,img = cv2.threshold(img,mean,255,cv2.THRESH_BINARY_INV)

    result = cv2.subtract(image,img)
    return result

# Allows me to import your script
if __name__ == "__main__":
    testImages = []
    testImages.append(cv2.imread('imgs/a.JPG', cv2.CV_LOAD_IMAGE_GRAYSCALE))
    testImages[0] = cv2.resize(testImages[0], (800, 600))


    #fnames = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
    fnames = ['a']
    testImages = []
    i = 0
    for letter in fnames:
        testImages.append(removePoolsLines(cv2.resize( cv2.imread('imgs/{}.JPG'.format(letter),0), (800, 600))))
        cv2.imshow('image{}'.format(i),testImages[i])
        time.sleep(1)
        i=i+1

    bilat = cv2.bilateralFilter(testImages[0], 20, 25,25)

    cv2.imshow('bilat',bilat)
    '''
    img = cv2.blur(testImages[0],(5,5))
    cv2.imshow('blur',img)
    sharpKernel = np.array([[-1, -1, -1],[-1, 9, -1], [-1,-1,-1]])
    edgeEnhance = np.array([[-1,-1,-1,-1,-1],
                                 [-1,2,2,2,-1],
                                 [-1,2,8,2,-1],
                                 [-1,2,2,2,-1],
                                 [-1,-1,-1,-1,-1]]) / 8.0
    #img = cv2.blur(img,(
    img = cv2.Canny(img,10,10)
    img = cv2.subtract(testImages[0],img)
    #img = cv2.filter2D(img,-1,sharpKernel)
    cv2.imshow('enhance',img)
    '''
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()

