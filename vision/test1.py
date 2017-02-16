import numpy as np
import cv2

fnames = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']

#testImages = []
#for letter in fnames:
#	testImages.append(cv2.imread('imgs/{}.JPG'.format(letter),0))
testImages = []
testImages.append(cv2.imread('imgs/a.JPG',))
testImages[0] = cv2.resize(testImages[0], (800,600))
cv2.imshow('image',testImages[0])

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
	cv2.destroyAllWindows()
