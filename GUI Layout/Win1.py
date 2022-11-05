import sys
import PyQt5
from PyQt5.QtWidgets import QApplication,  QWidget,  QLabel, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2


class Win1(QMainWindow):
    def __init__(self):
        super(Win1, self).__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        lay = QVBoxLayout(central_widget)
        self.DescLabel = QLabel("Win1")
        lay.addWidget(self.DescLabel)
        
        self.FeedLabel = QLabel()
        lay.addWidget(self.FeedLabel)

        #self.CancelBTN = QPushButton("Cancel")
        #self.CancelBTN.clicked.connect(self.CancelFeed)
        #self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()
        self.Worker2 = Worker2()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        #self.setLayout(self.VBL)
        self.showMaximized()


        self.Worker2.start()
        self.timer.setInterval(5000)
        self.timer.moveToThread(self.Worker2)
    
    def showWin2(self):
        Win2 = Win2.Win2()
        Win2.show()
        print ("Collecting Process Data")
        #Worker1.run()

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1920, 1080)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

class Worker2(QThread):
    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.timer = QTimer()
        self.timer.moveToThread(self)
        self.timer.timeout.connect(self.timer)


    def run(self):
        self.timer.start(1000)

        #loop = QEventLoop()
        #loop.exec_()
        
    #def run(self):
    #    self.timer.start(5000);

    def stop(self):
        self.ThreadActive = False
        self.quit()

