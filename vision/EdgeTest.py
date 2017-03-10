import cv2 as cv
import LearningModule as lMod

#---------------------------------
#    Testing script, do not import
if __name__ != "__main__":
    raise ImportError("Function is not to be imported!")
#---------------------------------

#Define track bar names
WIN_NAME         = 'CannyTest'
WIN_HUE_NAME     = 'HuePredict'
WIN_HUE_MSK_NAME = 'HueMasked'


C_LOW_BAR  = 'Low thresh'
C_HIGH_BAR = 'High thresh'
K_GAUSS    = 'Gauss sigma'
G_GAUSS    = 'Gauss radius'
K_MEDIAN   = 'Median Size'


# ========================================
# Initialize and process images
# ========================================
img_color = cv.imread('ProcessedImages/GOPR0041.jpg')
img = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
clf =  lMod.trainModel(lMod.buildDataSet())
print("Model built")

originalImage = img.copy()
imgHueMasked  = img.copy()
imgHue        = cv.cvtColor(lMod.getHuePrediction(img_color, clf),
                            cv.COLOR_BGR2GRAY)

#Variables used in pre-processing
cLowThresh  = 30
cHighThresh = 100
GaussSize   = (1, 1)
GaussK      = 1
medianK     = 1

#========================================
#   Call back methods
#========================================

def updateImage():
    global img
    global imgHueMasked
    # Updates an image according to variables from track bars
    imgBlurred = cv.GaussianBlur(originalImage, GaussSize, GaussK)
    img = cv.Canny(imgBlurred, cLowThresh, cHighThresh)

    #Mask the canny image vs Hue tested image
    imgHueMasked = (img > 10) * imgHue

#Test functions go here
def cannyLowThresh(r):
    global cLowThresh
    cLowThresh = r
    updateImage()

def cannyHighThresh(r):
    global cHighThresh
    cHighThresh = r
    updateImage()

def cannyGaussSize(r):
    global GaussSize
    #Don't allow odd values into gaussian blur
    if r % 2 == 0:
        r -= 1
    GaussSize = (r,r)
    updateImage()

def cannyGaussKSize(r):
    global GaussK
    GaussK = r
    updateImage()



# Track bar and window functionality
cv.imshow(WIN_HUE_NAME, imgHue)
cv.imshow(WIN_HUE_MSK_NAME, imgHueMasked)
cv.imshow(WIN_NAME, img)

cv.createTrackbar(C_LOW_BAR, WIN_NAME, 30, 200, cannyLowThresh)
cv.createTrackbar(C_HIGH_BAR, WIN_NAME, 100, 200, cannyHighThresh)
cv.createTrackbar(K_GAUSS, WIN_NAME, 1,10, cannyGaussKSize)
cv.createTrackbar(G_GAUSS, WIN_NAME, 5, 20, cannyGaussSize)


print("Entering update loop")

#Main loop
while True:
    cv.imshow(WIN_HUE_MSK_NAME, imgHueMasked)
    cv.imshow(WIN_NAME, img)
    k = cv.waitKey(16) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()