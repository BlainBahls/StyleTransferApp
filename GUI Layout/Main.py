from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

class Thread2(QThread):
    timer_finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.timer = QTimer()
        self.timer.start(5000) #normal value = 15000
        
    def run(self):
        print("Hello World")
        self.timer.timeout.connect(self.timer_finished)

    def stop(self):
        print("World Hello")
        self._run_flag = False
        self.wait()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 1920
        self.display_height = 1080
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Webcam')
        self.textLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        #self.showFullScreen()
        self.showFullScreen()

        self.window2 = Ui_SecondWindow()

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()
            
        self.thread2 = Thread2()
        self.currentWindow = 1
        self.thread2.timer_finished.connect(self.changeWindow)
        self.thread2.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def changeWindow(self):
        if self.currentWindow == 1:
            SecondWindow.showFullScreen()
            self.currentWindow = 2
        else:
            SecondWindow.showMinimized()
            self.currentWindow = 1


    #def showWindow1(self):
    #    self.window2.destroy()
       
#class SecondWindow(QMainWindow):
#    def __init__(self):
#        super(self.__class__, self).__init__()

#        self.central_widget = Ui_SecondWindow()
#        self.setCentralWidget(self.central_widget)


class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2175, 962)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_LaMuse_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_LaMuse_Original.setGeometry(QtCore.QRect(320, 240, 300, 300))
        self.graphicsView_LaMuse_Original.setStyleSheet("background-image: url(:/Resized/Resized Pictures/La Muse - Resized.jpg);")
        self.graphicsView_LaMuse_Original.setObjectName("graphicsView_LaMuse_Original")
        self.ArtWithMachineLearningLabel = QtWidgets.QLabel(self.centralwidget)
        self.ArtWithMachineLearningLabel.setGeometry(QtCore.QRect(0, 0, 2171, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.ArtWithMachineLearningLabel.setFont(font)
        self.ArtWithMachineLearningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ArtWithMachineLearningLabel.setObjectName("ArtWithMachineLearningLabel")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 2171, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.OriginalStyleLabel = QtWidgets.QLabel(self.centralwidget)
        self.OriginalStyleLabel.setGeometry(QtCore.QRect(0, 60, 2171, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.OriginalStyleLabel.setFont(font)
        self.OriginalStyleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OriginalStyleLabel.setObjectName("OriginalStyleLabel")
        self.YourStylizedResultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.YourStylizedResultsLabel.setGeometry(QtCore.QRect(0, 550, 2171, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.YourStylizedResultsLabel.setFont(font)
        self.YourStylizedResultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.YourStylizedResultsLabel.setObjectName("YourStylizedResultsLabel")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 540, 2171, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.graphicsView_Input_Picture = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Input_Picture.setGeometry(QtCore.QRect(10, 620, 300, 300))
        self.graphicsView_Input_Picture.setStyleSheet("background-image: url(:/Camera/Camera Photo/Input Picture.jpg);")
        self.graphicsView_Input_Picture.setObjectName("graphicsView_Input_Picture")
        self.LaMuseLabel = QtWidgets.QLabel(self.centralwidget)
        self.LaMuseLabel.setGeometry(QtCore.QRect(320, 120, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.LaMuseLabel.setFont(font)
        self.LaMuseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LaMuseLabel.setObjectName("LaMuseLabel")
        self.graphicsView_RainPrincess_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_RainPrincess_Original.setGeometry(QtCore.QRect(630, 240, 300, 300))
        self.graphicsView_RainPrincess_Original.setStyleSheet("background-image: url(:/Resized/Resized Pictures/Rain Princess - Resized.jpg);")
        self.graphicsView_RainPrincess_Original.setObjectName("graphicsView_RainPrincess_Original")
        self.PicassoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PicassoLabel.setGeometry(QtCore.QRect(320, 180, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.PicassoLabel.setFont(font)
        self.PicassoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PicassoLabel.setObjectName("PicassoLabel")
        self.RainPrincessLabel = QtWidgets.QLabel(self.centralwidget)
        self.RainPrincessLabel.setGeometry(QtCore.QRect(630, 120, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.RainPrincessLabel.setFont(font)
        self.RainPrincessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RainPrincessLabel.setObjectName("RainPrincessLabel")
        self.LeonidAfremovLabel = QtWidgets.QLabel(self.centralwidget)
        self.LeonidAfremovLabel.setGeometry(QtCore.QRect(630, 180, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.LeonidAfremovLabel.setFont(font)
        self.LeonidAfremovLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LeonidAfremovLabel.setObjectName("LeonidAfremovLabel")
        self.EdvardMunchLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdvardMunchLabel.setGeometry(QtCore.QRect(940, 180, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.EdvardMunchLabel.setFont(font)
        self.EdvardMunchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EdvardMunchLabel.setObjectName("EdvardMunchLabel")
        self.ScreamLabel = QtWidgets.QLabel(self.centralwidget)
        self.ScreamLabel.setGeometry(QtCore.QRect(940, 120, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.ScreamLabel.setFont(font)
        self.ScreamLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScreamLabel.setObjectName("ScreamLabel")
        self.graphicsView_Scream_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Original.setGeometry(QtCore.QRect(940, 240, 300, 300))
        self.graphicsView_Scream_Original.setStyleSheet("background-image: url(:/Resized/Resized Pictures/Scream - Resized.jpg);")
        self.graphicsView_Scream_Original.setObjectName("graphicsView_Scream_Original")
        self.VanGoghLabel = QtWidgets.QLabel(self.centralwidget)
        self.VanGoghLabel.setGeometry(QtCore.QRect(1250, 180, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.VanGoghLabel.setFont(font)
        self.VanGoghLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VanGoghLabel.setObjectName("VanGoghLabel")
        self.StarryNightLabel = QtWidgets.QLabel(self.centralwidget)
        self.StarryNightLabel.setGeometry(QtCore.QRect(1250, 120, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.StarryNightLabel.setFont(font)
        self.StarryNightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StarryNightLabel.setObjectName("StarryNightLabel")
        self.graphicsView_StarryNight_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_StarryNight_Original.setGeometry(QtCore.QRect(1250, 240, 300, 300))
        self.graphicsView_StarryNight_Original.setStyleSheet("background-image: url(:/Resized/Resized Pictures/Starry Night - Resized.jpg);")
        self.graphicsView_StarryNight_Original.setObjectName("graphicsView_StarryNight_Original")
        self.FrancisPicabiaLabel = QtWidgets.QLabel(self.centralwidget)
        self.FrancisPicabiaLabel.setGeometry(QtCore.QRect(1560, 180, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.FrancisPicabiaLabel.setFont(font)
        self.FrancisPicabiaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FrancisPicabiaLabel.setObjectName("FrancisPicabiaLabel")
        self.UdnieLabel = QtWidgets.QLabel(self.centralwidget)
        self.UdnieLabel.setGeometry(QtCore.QRect(1560, 120, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.UdnieLabel.setFont(font)
        self.UdnieLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UdnieLabel.setObjectName("UdnieLabel")
        self.graphicsView_Udnie_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Udnie_Original.setGeometry(QtCore.QRect(1560, 240, 300, 300))
        self.graphicsView_Udnie_Original.setStyleSheet("background-image: url(:/Resized/Resized Pictures/Udnie - Resized.jpg);")
        self.graphicsView_Udnie_Original.setObjectName("graphicsView_Udnie_Original")
        self.HokusaiLabel = QtWidgets.QLabel(self.centralwidget)
        self.HokusaiLabel.setGeometry(QtCore.QRect(1870, 180, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.HokusaiLabel.setFont(font)
        self.HokusaiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HokusaiLabel.setObjectName("HokusaiLabel")
        self.GreatWaveLabel = QtWidgets.QLabel(self.centralwidget)
        self.GreatWaveLabel.setGeometry(QtCore.QRect(1870, 120, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        self.GreatWaveLabel.setFont(font)
        self.GreatWaveLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GreatWaveLabel.setObjectName("GreatWaveLabel")
        self.graphicsView_GreatWave_Original = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_GreatWave_Original.setGeometry(QtCore.QRect(1870, 240, 300, 300))
        self.graphicsView_GreatWave_Original.setStyleSheet("background-image: url(:/Resized/Resized Pictures/Great Wave - Resized.jpg);")
        self.graphicsView_GreatWave_Original.setObjectName("graphicsView_GreatWave_Original")
        self.graphicsView_LaMuse_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_LaMuse_Stylized.setGeometry(QtCore.QRect(320, 620, 300, 300))
        self.graphicsView_LaMuse_Stylized.setStyleSheet("background-image: url(:/Stylized/Stylized Pictures/Stylized La Muse.jpg);")
        self.graphicsView_LaMuse_Stylized.setObjectName("graphicsView_LaMuse_Stylized")
        self.graphicsView_Udnie_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Udnie_Stylized.setGeometry(QtCore.QRect(1560, 620, 300, 300))
        self.graphicsView_Udnie_Stylized.setStyleSheet("background-image: url(:/Stylized/Stylized Pictures/Stylized Udnie.jpg);")
        self.graphicsView_Udnie_Stylized.setObjectName("graphicsView_Udnie_Stylized")
        self.graphicsView_GreatWave_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_GreatWave_Stylized.setGeometry(QtCore.QRect(1870, 620, 300, 300))
        self.graphicsView_GreatWave_Stylized.setStyleSheet("background-image: url(:/Stylized/Stylized Pictures/Stylized Great Wave.jpg);")
        self.graphicsView_GreatWave_Stylized.setObjectName("graphicsView_GreatWave_Stylized")
        self.graphicsView_RainPrincess_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_RainPrincess_Stylized.setGeometry(QtCore.QRect(630, 620, 300, 300))
        self.graphicsView_RainPrincess_Stylized.setStyleSheet("background-image: url(:/Stylized/Stylized Pictures/Stylized Rain Princess.jpg);")
        self.graphicsView_RainPrincess_Stylized.setObjectName("graphicsView_RainPrincess_Stylized")
        self.graphicsView_Scream_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Scream_Stylized.setGeometry(QtCore.QRect(940, 620, 300, 300))
        self.graphicsView_Scream_Stylized.setStyleSheet("background-image: url(:/Stylized/Stylized Pictures/Stylized Scream.jpg);")
        self.graphicsView_Scream_Stylized.setObjectName("graphicsView_Scream_Stylized")
        self.graphicsView_StarryNight_Stylized = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_StarryNight_Stylized.setGeometry(QtCore.QRect(1250, 620, 300, 300))
        self.graphicsView_StarryNight_Stylized.setStyleSheet("background-image: url(:/Stylized/Stylized Pictures/Stylized Starry Night.jpg);")
        self.graphicsView_StarryNight_Stylized.setObjectName("graphicsView_StarryNight_Stylized")
        self.graphicsView_Input_Picture_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_Input_Picture_2.setGeometry(QtCore.QRect(10, 240, 300, 300))
        self.graphicsView_Input_Picture_2.setStyleSheet("background-image: url(:/Logos/Logos/index.png);")
        self.graphicsView_Input_Picture_2.setObjectName("graphicsView_Input_Picture_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2175, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ArtWithMachineLearningLabel.setText(_translate("MainWindow", "Art With Machine Learning"))
        self.OriginalStyleLabel.setText(_translate("MainWindow", "Original Styles"))
        self.YourStylizedResultsLabel.setText(_translate("MainWindow", "Your Stylized Results!"))
        self.LaMuseLabel.setText(_translate("MainWindow", "Picasso\'s"))
        self.PicassoLabel.setText(_translate("MainWindow", "La Muse"))
        self.RainPrincessLabel.setText(_translate("MainWindow", "Leonid Afremov\'s"))
        self.LeonidAfremovLabel.setText(_translate("MainWindow", "Rain Princess"))
        self.EdvardMunchLabel.setText(_translate("MainWindow", "The Scream"))
        self.ScreamLabel.setText(_translate("MainWindow", "Edvard Munch\'s"))
        self.VanGoghLabel.setText(_translate("MainWindow", "Starry Night"))
        self.StarryNightLabel.setText(_translate("MainWindow", "Van Gogh\'s"))
        self.FrancisPicabiaLabel.setText(_translate("MainWindow", "Udnie"))
        self.UdnieLabel.setText(_translate("MainWindow", "Francis Picabia\'s"))
        self.HokusaiLabel.setText(_translate("MainWindow", "Great Wave"))
        self.GreatWaveLabel.setText(_translate("MainWindow", "Hokusai\'s"))
#sys.path.insert(1, 'C:/Users/brend/source/repos/BlainBahls/StyleTransferApp/Images/ImageResourceFile.py')
import ImageResourceFile

if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    a.show()
    sys.exit(app.exec_())
