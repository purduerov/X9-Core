import json
import cv2 as cv
from random import shuffle
import math
import sklearn.metrics as metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import operator
import random
import test2



#=========================================================
#                    Build Dataset
#==========================================================
with open('slothOut.json') as slothLabels:
    imageAnnotations = json.load(slothLabels)

#Annnnnd this is a memory hog :)
dataset=[]

#Create dataset from training images
for imageAnnotation in imageAnnotations:
    imgFilename = imageAnnotation["filename"]
    img = cv.imread(imgFilename)
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
    # TODO try normalizing the color ahead of time
    img = cv.medianBlur(img, 7)
    img = cv.blur(img, (5,5))


    for annotation in imageAnnotation["annotations"]:
        x = int(round(annotation["y"]))
        y = int(round(annotation["x"]))
        positive = False
        if annotation["class"] == "positive":
            positive = True
        dataset.append([img[x][y].tolist(), positive])

#==========================================================
#              Begin Machine learning
#==========================================================

#Shake the data up
shuffle(dataset,random=random.seed(a=3))

#Split between features and labels
features, labels = zip(*dataset)

features = list(features)
labels = list(labels)

print "There are {0} features".format(len(features))
percent_test = .3

len_train = int(math.ceil(len(features) * (1-percent_test)))

#Split out the training features
features_train = features[0:len_train]
labels_train   = labels[0:len_train]

#Split out the test features
features_test = features[len_train::]
labels_test   = labels[len_train::]

assert(len(features_test) + len(features_train) == len(dataset))

# Probably am going to want to increase the precision score with
# a CVGridSearch for best parameters possible


# TODO These args need to be tweaked and the algorithm needs some cleaning up
tree = DecisionTreeClassifier(max_depth=1, min_samples_leaf=2,
                              min_samples_split=10, random_state=1)
clf = AdaBoostClassifier(tree, n_estimators=100, random_state=1)

clf = GradientBoostingClassifier(random_state=1)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print "Accuracy:  {0:.3}".format(metrics.accuracy_score(labels_test, pred))
print "Recall:    {0:.3}".format(metrics.recall_score(labels_test, pred))
print "Precision: {0:.3}".format(metrics.precision_score(labels_test, pred))


# Now to run on image and see what happens. What metric is best
# to determine the quality of this algorithm? Should I try a
# grid search then stratified kFold?
# Need to test before and after bilateral filter is applied


img = cv.imread('ProcessedImages/GOPR0031.jpg')
#img = cv.blur(img, (7,7))
#img = test2.removePoolsLines(img)
#Input Pre-processing
img = cv.medianBlur(img, 5)
#img = cv.bilateralFilter(img, 10, 25,25)
cv.imshow("Pre-Processed", img)

#==============================================
#             Image pre-processing

#img = cv.bilateralFilter(img, 15, 30,12)
img = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
#TODO: HELP PROCESS THE IMAGE!! Morphological operations should be done here

#=============================================
#Reshape and predict
rows, cols,_ = img.shape
flatImg = img.reshape(rows*cols, 3)
pred = clf.predict(flatImg)

maskedImg = np.array(map(operator.mul,pred, flatImg))

#Rebuild image
maskedImg = maskedImg.reshape(rows, cols, 3)
maskedImg = cv.cvtColor(maskedImg, cv.COLOR_HSV2BGR_FULL)

#===================================================
#                End Machine Learning
#===================================================

#Present!
cv.imshow("Predicted", maskedImg)

postImg = cv.cvtColor(maskedImg,cv.COLOR_BGR2GRAY)
postImg = cv.medianBlur(postImg, 5)

cv.imshow("Post Processed", postImg)
#Put a timeout on how long the image shows so it doesn't stay running
cv.waitKey()
