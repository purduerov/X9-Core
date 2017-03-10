import json
import cv2 as cv
from random import shuffle
import math
import sklearn.metrics as metrics
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import operator
import random
import glob

""" Builds the data set for the machine learning model from sloth out.json"""
def buildDataSet():
    if not glob.glob('slothOut.json'):
        raise OSError("SlothOut.json not found")

    with open('slothOut.json') as slothLabels:
        imageAnnotations = json.load(slothLabels)

    #Annnnnd this is a memory hog :)
    data_set=[]

    #Create data set from training images
    for imageAnnotation in imageAnnotations:
        imgFilename = imageAnnotation["filename"]
        img = cv.imread(imgFilename)
        img = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
        # TODO try normalizing the color ahead of time
        # TODO The hsv color space is NOT normalized! Saturation is largest
        img = cv.medianBlur(img, 7)
        img = cv.blur(img, (5,5))


        for annotation in imageAnnotation["annotations"]:
            x = int(round(annotation["y"]))
            y = int(round(annotation["x"]))
            positive = False
            if annotation["class"] == "positive":
                positive = True
            data_set.append([img[x][y].tolist(), positive])
    return data_set

"""
    Trains the learning model on the testing set.
"""
def trainModel(data_set):
    if not data_set:
        raise ValueError("Dataset variable is empty")
    #Shake the data up
    shuffle(data_set, random=random.seed(a=3))

    #Split between features and labels
    features, labels = zip(*data_set)

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

    assert(len(features_test) + len(features_train) == len(data_set))

    # CVGridSearch for best parameters possible
    # Stratified KFold training may be good
    # Pipeline with some feature processing should go here


    clf = GradientBoostingClassifier(random_state=1)
    clf.fit(features_train, labels_train)

    return clf


"""
    Masks the classifier prediction of the input image against the image
    itself. Returns an image containing pixels that the classifier
    predicts are part of the box. Takes in a 3 channel image and returns
    a 3 channel image
"""
def getHuePrediction(img, clf):
    #Reshape and predict
    rows, cols,_ = img.shape
    flatImg = img.reshape(rows*cols, 3)
    pred = clf.predict(flatImg)

    maskedImg = np.array(map(operator.mul,pred, flatImg))

    #Rebuild image
    maskedImg = maskedImg.reshape(rows, cols, 3)
    return maskedImg


# TODO Write some test cases!
if __name__ == "__main__":
    # pred = clf.predict(features_test)
    # print "Accuracy:  {0:.3}".format(metrics.accuracy_score(labels_test, pred))
    # print "Recall:    {0:.3}".format(metrics.recall_score(labels_test, pred))
    # print "Precision: {0:.3}".format(metrics.precision_score(labels_test, pred))
    pass


