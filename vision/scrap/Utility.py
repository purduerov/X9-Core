
import glob
import os
from PIL import Image


#Quick script to resize images into an output directory
def resizeImages(dirIn, dirOut):

    # CREDIT: http://stackoverflow.com/questions/4568580/python-glob-multiple-filetypes
    filetypes = ['*.png', '*.jpg', '*.JPG', '*.PNG']
    files = []
    for type in filetypes:
        files.extend(glob.glob(dirIn + "/" + type))

    for imageFile in files:
        im = Image.open(imageFile)
        im.thumbnail((400, 400), Image.ANTIALIAS)

        filename = os.path.split(os.path.splitext(imageFile)[0])[1]
        im.save(dirOut + "/" + filename + ".jpg", "JPEG")


#Converts paths to unix file paths
def convertPathsToUnix(pathToJsonFile):
    with open(pathToJsonFile, 'r') as slothOut:
        lines = slothOut.readlines()
        for i in range(len(lines)):
            if lines[i].find("\\\\") != -1:
                print lines[i]
                lines[i] = lines[i].replace("\\\\", "/")
                print " >>" + lines[i]

    if not lines:
        print "Error converting paths"
        return

    with open(pathToJsonFile, 'w') as slothOut:
        slothOut.writelines(lines)


if __name__ == "__main__":
    #resizeImages("RAW Images", "ProcessedImages")
    convertPathsToUnix("slothOut.json")
