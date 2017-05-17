from mainwindow import *
from PySide.QtGui import *
import numpy as np
import math
import itertools as it
from MeasureUtility import *
from math import sqrt
import networkx as nx

class MainGui(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainGui, self).__init__(parent)
        self.setupUi(self)

        self.btnLabelContainers.clicked.connect(self.labelContainers)
        self.btnCapture.clicked.connect(self.capture)
        self.btnMeasureDone.clicked.connect(self.measureDone)

        # Measure toolbox
        self.btnFind1.clicked.connect(lambda : self.findPoints(self.btnFind1, self.lblDist1, self.lblAngle1, 0))
        self.btnFind2.clicked.connect(lambda : self.findPoints(self.btnFind2, self.lblDist2, self.lblAngle2, 1))
        self.btnFind3.clicked.connect(lambda : self.findPoints(self.btnFind3, self.lblDist3, self.lblAngle3, 2))

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
        self.operationsTabWidget.setCurrentIndex(0)
        self.mainTabWidget.setTabEnabled(1,False)

        # Class variables
        self.grabMeasClicks = False
        self.measClicks = []
        self.activeFind=  None
        self.activeAngle = None
        self.activeDist = None

        self.grabMapClicks = False

        self.mapClicks = [] #Ordered array of user's clicks on map

        self.MAP_INDEX = 0
        self.MEAS_INDEX = 1

        self.measEdges = [0,0,0]
        self.activeEdge = 0
        self.edges = None

    def measureDone(self):
        if self.lblDist1.text == "":
            return
        if self.lblDist2.text == "":
            return
        if self.lblDist3.text == "":
            return

        self.cleanMapGraphics()
        print(self.mapClicks)

        #Specified as float so np doesn't freak
        hCoord =  (float(self.mapClicks[0][0].x()), float(self.mapClicks[0][0].y()))
        print(hCoord)
        coords = getRealCoordinatesOfPoints(self.edges, self.measEdges, hCoord)
        for c in coords:
            self.mapGView.scene().addEllipse(c[0]-2,c[1]-2, 4,4, QPen(QtCore.Qt.green))
            self.mapGView.scene().addLine(hCoord[0], hCoord[1], c[0],c[1], QPen(QtCore.Qt.blue))

    def mapGViewMousePress(self, e):
        if not self.grabMapClicks:
            return

        pos = QtCore.QPointF(e.scenePos())

        item = None
        if len(self.mapClicks) == 0:
            item = QGraphicsTextItem("High Risk")
            self.mapClicks.append((pos,'H'))

        elif len(self.mapClicks) == 1:
            item = QGraphicsTextItem("A")
            self.mapClicks.append((pos,'A'))

        elif len(self.mapClicks) == 2:
            item = QGraphicsTextItem("B")
            self.mapClicks.append((pos,'B'))

        elif len(self.mapClicks) == 3:
            item = QGraphicsTextItem("C")
            self.mapClicks.append((pos,'C'))
            self.btnLabelContainers.setText("Label Containers")
            self.grabMapClicks = False
            self.setUpMeasurement(self.createInitialGraph())

        item.setPos(pos.x()-10, pos.y()-10)
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

    def setUpMeasurement(self, edges):
        self.mainTabWidget.setTabEnabled(1, True)
        lbls = [self.lblMeas1, self.lblMeas2, self.lblMeas3]
        for i in range(3):
            edge = edges[i]
            lbl = lbls[i]
            lbl.setText("{0} -> {1}".format(edge[0][2],edge[1][2]))
        self.edges = edges
        print(edges)

    def createInitialGraph(self):
        G = nx.Graph()
        b = [(x[0].x(), x[0].y(), x[1]) for x in self.mapClicks]
        G.add_nodes_from(b)
        combs = list(it.combinations(G.nodes(), 2))
        weights = [sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) for p1, p2 in combs]
        wDict = [{'weight': w} for w in weights]
        edges = list(map(lambda a: (a[0][0], a[0][1], a[1]), zip(combs, wDict)))
        G.add_edges_from(edges)
        edges = nx.minimum_spanning_edges(G)
        mst = nx.minimum_spanning_tree(G)


        for edge in edges:
            self.mapGView.scene().addLine(edge[0][0], edge[0][1], edge[1][0], edge[1][1], QPen(QtCore.Qt.blue))
        return list(nx.bfs_edges(mst, mst.nodes()[0]))


    def capture(self):
        if self.mainTabWidget.currentIndex() == self.MAP_INDEX:
            self.loadMapImage()

        if self.mainTabWidget.currentIndex() == self.MEAS_INDEX:
            self.loadMeasImage(self.mainGView)

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
    def findPoints(self, btn, angle, dist, activeEdgeIndex):
        [x.setDisabled(True) for x in [self.btnFind1, self.btnFind2, self.btnFind3]]
        btn.setEnabled(True)

        self.cleanMeasGraphics()
        self.measClicks = []
        self.activeFind = btn
        self.activeAngle = angle
        self.activeDist = dist

        if btn.text() == "O":
            self.grabMeasClicks = True
            self.activeEdge = activeEdgeIndex
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

        dist = math.sqrt((centerX1-centerX)**2 + (centerY-centerY1)**2)
        self.measEdges[self.activeEdge] = dist
        self.activeDist.setText("{:.2f}px".format(dist))

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
