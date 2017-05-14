import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img_scene = cv.imread("RDTestImages/IMG_0398.jpg")
img_object = cv.imread("RDTestImages/side.jpg")
img_object = cv.medianBlur(img_object,3)

#Get keypoints and descriptors
detector = cv.xfeatures2d.SURF_create(300)
kp_obj, dsc_obj  = detector.detectAndCompute(img_object, None )
kp_scene, dsc_scn = detector.detectAndCompute(img_scene, None )

# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html
# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv.FlannBasedMatcher(index_params,search_params)

#Match keypoints and descriptors
matches = flann.knnMatch(dsc_obj, dsc_scn,k=2)


#H = cv.findHomography(kp_obj, kp_scene, cv.RANSAC)



#plt.imshow(img3,),plt.show()
#img3 = cv.drawMatchesKnn(img_object,kp_obj,img_scene,kp_scene,matches,None,**draw_params)
