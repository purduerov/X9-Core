from mainwindow import *
from PySide.QtGui import *
import sys
import numpy as np
import math

class MainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainGui, self).__init__(parent)
        self.setupUi(self)

        self.btnCapture.clicked.connect(self.capture)
        self.btnFind1.clicked.connect(lambda : self.findPoints(self.btnFind1, self.lblDist1, self.lblAngle1))
        self.btnFind2.clicked.connect(lambda : self.findPoints(self.btnFind2, self.lblDist2, self.lblAngle2))
        self.btnFind3.clicked.connect(lambda : self.findPoints(self.btnFind3, self.lblDist3, self.lblAngle3))
        self.mainGView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainGView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainGView.scrollContentsBy = self.scrollContents

        #Class variables
        self.grabbingClicks = False
        self.clicksGrabbed = []
        self.activeFind=  None
        self.activeAngle = None
        self.activeDist = None

    def capture(self):
        #This should capture the current video feed
        self.loadImage()


    def scrollContents(self, *args, **kwargs):
        #Do nothing, this prevents the image from scrolling and messing up measurements
        pass

    """Initiates a sequence to obtain points to measure distance"""
    def findPoints(self, btn, angle, dist):
        [x.setDisabled(True) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]
        btn.setEnabled(True)

        self.cleanGraphics()
        self.clicksGrabbed = []
        self.activeFind = btn
        self.activeAngle = angle
        self.activeDist = dist

        if btn.text() == "O":
            self.grabbingClicks = True
            btn.setText("X")
            angle.setText("---")
            dist.setText("---")
        else:
            [x.setDisabled(False) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]
            btn.setText("O")
            self.grabbingClicks = False
            angle.setText("---")
            dist.setText("---")

    def sceneMousePressEvent(self, e):
        if not self.grabbingClicks:
            return

        pos = QtCore.QPointF(e.scenePos())
        self.mainGView.scene().addEllipse(pos.x()-2, pos.y()-2, 4,4, QPen(QtCore.Qt.green))
        self.mainGView.show()
        self.clicksGrabbed.append((pos.x(), pos.y()))

        #Removes all items on the graphics view except for the image which is last item in array
        if len(self.clicksGrabbed) == 4:
            self.computeFourClicks()

        if len(self.clicksGrabbed) == 8:
            self.compute8Clicks()

    def computeFourClicks(self):
        centerX, centerY = computeCenter(self.clicksGrabbed[0:4])
        self.mainGView.scene().addEllipse(centerX - 2, centerY-2, 4,4, QPen(QtCore.Qt.blue))
        self.mainGView.show()

    def compute8Clicks(self):
        centerX, centerY = computeCenter(self.clicksGrabbed[4:8])
        self.mainGView.scene().addEllipse(centerX - 2, centerY-2, 4,4, QPen(QtCore.Qt.blue))
        centerX1, centerY1 = computeCenter(self.clicksGrabbed[0:4])
        self.mainGView.scene().addLine(centerX1, centerY1, centerX, centerY, QPen(QtCore.Qt.blue))
        self.mainGView.show()
        self.activeFind.setText("O")
        self.grabbingClicks = False

        self.activeAngle.setText("{:.2f}px".format(math.sqrt((centerX1-centerX)**2 + (centerY-centerY1)**2)))
        self.clicksGrabbed = []
        [x.setDisabled(False) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]

    #Clean everything in the main graphics view except for the picture
    def cleanGraphics(self):
        [self.mainGView.scene().removeItem(item) for item in self.mainGView.items()[0:-1]]

    def loadImage(self):
        #TODO this function will eventually be responsible for streaming a video
        self.mainGView.setScene(QGraphicsScene())
        graphItem = QGraphicsPixmapItem(QPixmap("ProcessedImages/GOPR0034"))
        self.mainGView.scene().addItem(graphItem)
        self.mainGView.fitInView(graphItem, QtCore.Qt.KeepAspectRatioByExpanding)
        self.mainGView.show()
        self.mainGView.scene().mousePressEvent = self.sceneMousePressEvent


#   ---------------------------------------
#        Static utility functions below
#   ---------------------------------------

def NpToQt(raw_img):
    (height, width, _) = raw_img.shape
    #Code to convert from QT to np
    img = np.array(raw_img, dtype=np.uint32)
    img_data = ( img[:,:,2] | img[:,:,1]<<8 | img[:,:,0] << 16) #Using BGR format
    img = QImage(img_data, height, width, QImage.Format_RGB32)
    return img

"""Computes the center of an array of points"""
def computeCenter(arr):
    xKey = lambda x: x[0]
    yKey = lambda y: y[1]
    centerX = int((max(arr, key=xKey)[0] + min(arr, key=xKey)[0]) / 2)
    centerY = int((max(arr, key=yKey)[1] + min(arr, key=yKey)[1]) / 2)

    return centerX, centerY

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MainGui()
    currentForm.show()
    currentApp.exec_()

