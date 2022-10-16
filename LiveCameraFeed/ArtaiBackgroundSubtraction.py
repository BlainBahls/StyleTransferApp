# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:13:17 2022

@author: trr2
"""
#imports
import numpy as np
import cv2

#variable declaration.
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorKNN()

while True:
#instantiate frame to cap.read() - which will return the image itself.  
    ret, frame = cap.read()

#instantiate fgmask with the fgbg variable being applied to the frame.
    fgmask = fgbg.apply(frame)

#shows image capture and applies fgmask to it - fgmask is the background subtractor.
    cv2.imshow('frame', fgmask)
    
#this will end the window from capturing by pressing 'q'.
    if cv2.waitKey(1) == ord('q'):
        break

#after the 'q' key is pressed, release and destroy all windows, closing the program.
cap.release()
cv2.destroyAllWindows()