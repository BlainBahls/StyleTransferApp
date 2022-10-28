import sys
from PyQt5.QtWidgets import QApplication,  QWidget,  QLabel, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import Win1
import Win2
import time


timer=QTimer()

App = QApplication(sys.argv)
Win1 = Win1.Win1()
Win2 = Win2.Win2()
#Win1.show()
#Win2.show()
currentWindow = 1

timer.start(5000)
while True:
    if timer.remainingTime() == 0:
        timer.start(5000)
        if currentWindow == 2:
            currentWindow = 1
            Win1.show()
            Win2.close()
        if currentWindow == 1:
            currentWindow = 2
            Win2.show()
            Win1.close()
    #QtCore.QTimer.singleShot(3000, self.clear_win)
    print(timer.remainingTime())

    


def cameraFeed():
    Win1.show()

def pictureCycle():
    Win2.show()



#Win2.show()
cameraFeed()
#pictureCycle()
sys.exit(App.exec())
#suh