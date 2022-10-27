import sys
from PyQt5.QtWidgets import QApplication,  QWidget,  QLabel, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import Win1
import Win2

App = QApplication(sys.argv)
Win1 = Win1.Win1()
#Win2 = Win2.Win2()
Win1.show()
#Win2.show()
sys.exit(App.exec())
#suh