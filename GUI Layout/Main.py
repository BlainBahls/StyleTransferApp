import sys
from PyQt5.QtWidgets import QApplication,  QWidget,  QLabel, QMainWindow, QPushButton, QAction
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import Win1
import Win2
import time
from threading import Timer

#timer=QTimer()

App = QApplication(sys.argv)
Win1 = Win1.Win1()
Win2 = Win2.Win2()
#Win1.show()
#Win2.show()
currentWindow = 1

#timer.start(5000)
#-----------------------------------------------------------------------------------------|
def cameraFeed():
    Win1.show()

def pictureCycle():
    Win2.show()

# Create a function that will print the time
def create_countdown_timer(time):
    print(time,"......")

time_in_sec=5
App.exec()
while True:
    
    for times in range(time_in_sec):
        # call the function and pass the current time left
        create_countdown_timer(time_in_sec-times)
        # call the function in every 1 second.
        time.sleep(1)
  
    print("Time is up. Execute Window Activation here: \nPicture is Taken.")
    print("Windows 1 ceases and Window 2 is activated to show stylized picture.")
    cameraFeed()
    
    for times in range(time_in_sec):
        # call the function and pass the current time left
        create_countdown_timer(time_in_sec-times)
        # call the function in every 1 second.
        time.sleep(1)

    print("Time is up. Execute Window Activation here:\nMove back to Live Camera Feed.")
    print("Windows 2 ceases and Window 1 is activated.")
    pictureCycle()
#------------------------------------------------------------------------------------------|    
    #def func1():
    #    print("This is window 1.","\n")
    #    Win1.show()
        
    #def func2():
    #    print("This is window 2.","\n")
    #    Win2.show()
    #App.exec()
    #t1 = Timer(interval=3.0,function=func1)
    #t2 = Timer(interval=6.0,function=func2)
    
    #t1.start()
    #t2.start()
    
    


    #if timer.remainingTime() == 0:
    #    timer.start(5000)
    #    if currentWindow == 2:
    #        currentWindow = 1
    #        Win1.show()
    #        Win2.close()
    #    if currentWindow == 1:
    #        currentWindow = 2
    #        Win2.show()
    #        Win1.close()
    ##QtCore.QTimer.singleShot(3000, self.clear_win)
    #print(timer.remainingTime())

    


def cameraFeed():
    Win1.show()

def pictureCycle():
    Win2.show()



#Win2.show()
cameraFeed()
#pictureCycle()
sys.exit(App.exec())
#suh