from mainwindow import *
from PySide.QtGui import *
import sys
import numpy as np
import math

class MainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainGui, self).__init__(parent)
        self.setupUi(self)

        self.btnLabelContainers.clicked.connect(self.labelContainers)
        self.btnCapture.clicked.connect(self.capture)

        # Measure toolbox
        self.btnFind1.clicked.connect(lambda : self.findPoints(self.btnFind1, self.lblDist1, self.lblAngle1))
        self.btnFind2.clicked.connect(lambda : self.findPoints(self.btnFind2, self.lblDist2, self.lblAngle2))
        self.btnFind3.clicked.connect(lambda : self.findPoints(self.btnFind3, self.lblDist3, self.lblAngle3))

        # Customize graphics views
        self.mainGView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainGView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mainGView.scrollContentsBy = self.scrollContents
        self.mapGView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mapGView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mapGView.scrollContentsBy = self.scrollContents

        # Set up tab widgets
        self.mainTabWidget.currentChanged.connect(self.mainTabChangedEvent)
        self.operationsTabWidget.currentChanged.connect(self.operationsTabChangeEvent)

        # Class variables
        self.grabMeasClicks = False
        self.measClicks = []
        self.activeFind=  None
        self.activeAngle = None
        self.activeDist = None

        self.grabMapClicks = False
        self.mapClicks = []

        self.MAP_INDEX = 0
        self.MEAS_INDEX = 1



    def mapGViewMousePress(self, e):
        if not self.grabMapClicks:
            return

        pos = QtCore.QPointF(e.scenePos())
        self.mapClicks.append(pos)

        if len(self.mapClicks) == 1:
            item = QGraphicsTextItem("High Risk")

        if len(self.mapClicks) == 2:
            item = QGraphicsTextItem("A")
        if len(self.mapClicks) == 3:
            item = QGraphicsTextItem("B")

        if len(self.mapClicks) == 4:
            item = QGraphicsTextItem("C")
            self.btnLabelContainers.setText("Label Containers")
            self.grabMapClicks = False
            self.createGraph()

        item.setPos(pos.x(), pos.y())
        item.setFont(QFont(pointSize=60))
        item.setDefaultTextColor(QtCore.Qt.green)
        self.mapGView.scene().addItem(item)

    def labelContainers(self):
        self.cleanMapGraphics()
        if not self.grabMapClicks:
            self.grabMapClicks = True
            self.mapClicks = []
            self.btnLabelContainers.setText("Labelling")
        else:
            self.grabMapClicks = False
            self.mapClicks = []
            self.btnLabelContainers.setText("Label Containers")

    def createGraph(self):
        # TODO this function is responsible for creating a graph of all of the elements and updating the text
        # in the measurement tool
        pass


    def capture(self):
        if self.mainTabWidget.currentIndex() == self.MAP_INDEX:
            self.loadMapImage()
            print("LoadingGView")

        if self.mainTabWidget.currentIndex() == self.MEAS_INDEX:
            self.loadMeasImage(self.mainGView)
            print("LoadingGView1")

    def scrollContents(self, *args, **kwargs):
        #Do nothing, this prevents the image from scrolling and messing up measurements
        pass

    def mainTabChangedEvent(self, i):
        # Stupid proof tab changing
        if self.grabMeasClicks:
            self.mainTabWidget.setCurrentIndex(1)
            return
        if self.grabMapClicks:
            self.mainTabWidget.setCurrentIndex(0)
            return
        self.operationsTabWidget.setCurrentIndex(i)

    def operationsTabChangeEvent(self, _):
        self.operationsTabWidget.setCurrentIndex(self.mainTabWidget.currentIndex())

    """Initiates a sequence to obtain points to measure distance"""
    def findPoints(self, btn, angle, dist):
        [x.setDisabled(True) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]
        btn.setEnabled(True)

        self.cleanMeasGraphics()
        self.measClicks = []
        self.activeFind = btn
        self.activeAngle = angle
        self.activeDist = dist

        if btn.text() == "O":
            self.grabMeasClicks = True
            btn.setText("X")
            angle.setText("---")
            dist.setText("---")
        else:
            [x.setDisabled(False) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]
            btn.setText("O")
            self.grabMeasClicks = False
            angle.setText("---")
            dist.setText("---")

    def sceneMousePressEvent(self, e):
        if not self.grabMeasClicks:
            return

        pos = QtCore.QPointF(e.scenePos())
        self.mainGView.scene().addEllipse(pos.x()-2, pos.y()-2, 4,4, QPen(QtCore.Qt.green))
        self.mainGView.show()
        self.measClicks.append((pos.x(), pos.y()))

        #Removes all items on the graphics view except for the image which is last item in array
        if len(self.measClicks) == 4:
            self.computeFourClicks()

        if len(self.measClicks) == 8:
            self.compute8Clicks()

    def computeFourClicks(self):
        centerX, centerY = computeCenter(self.measClicks[0:4])
        self.mainGView.scene().addEllipse(centerX - 2, centerY-2, 4,4, QPen(QtCore.Qt.blue))
        self.mainGView.show()

    def compute8Clicks(self):
        centerX, centerY = computeCenter(self.measClicks[4:8])
        self.mainGView.scene().addEllipse(centerX - 2, centerY-2, 4,4, QPen(QtCore.Qt.blue))
        centerX1, centerY1 = computeCenter(self.measClicks[0:4])
        self.mainGView.scene().addLine(centerX1, centerY1, centerX, centerY, QPen(QtCore.Qt.blue))
        self.mainGView.show()
        self.activeFind.setText("O")
        self.grabMeasClicks = False

        self.activeDist.setText("{:.2f}px".format(math.sqrt((centerX1-centerX)**2 + (centerY-centerY1)**2)))

        coords = sorted([(centerX, centerY), (centerX1, centerY1)], key = lambda x: x[0])
        self.activeAngle.setText("{:.2f}deg".format(
            math.degrees(math.atan((coords[0][1]- coords[1][1]) / (coords[1][0] - coords[0][0])))))

        #Clean up
        self.measClicks = []
        [x.setDisabled(False) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]

    #Clean everything in the main graphics view except for the picture
    def cleanMeasGraphics(self):
        [self.mainGView.scene().removeItem(item) for item in self.mainGView.items()[0:-1]]
    def cleanMapGraphics(self):
        [self.mapGView.scene().removeItem(item) for item in self.mapGView.items()[0:-1]]


    def loadMapImage(self):
        #TODO connect this to a dummy class that can be hooked up to web server
        self.mapGView.setScene(QGraphicsScene())
        graphItem = QGraphicsPixmapItem(QPixmap("ProcessedImages/GOPR0034"))
        self.mapGView.scene().addItem(graphItem)
        self.mapGView.fitInView(graphItem, QtCore.Qt.KeepAspectRatio)
        self.mapGView.show()
        self.mapGView.scene().mousePressEvent = self.mapGViewMousePress

    def loadMeasImage(self, gView):
        #TODO this function will eventually be responsible for streaming a video
        gView.setScene(QGraphicsScene())
        graphItem = QGraphicsPixmapItem(QPixmap("ProcessedImages/GOPR0034"))
        gView.scene().addItem(graphItem)
        gView.fitInView(graphItem, QtCore.Qt.KeepAspectRatioByExpanding)
        gView.show()
        gView.scene().mousePressEvent = self.sceneMousePressEvent


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
    currentApp = QApplication("Container Measurement")
    currentForm = MainGui()
    currentForm.show()
    currentApp.exec_()
