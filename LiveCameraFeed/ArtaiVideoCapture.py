# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:47:02 2022

@author: trr2
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  #returns the image itself using read(), a numpy array
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):  #this will end the window from capturing
        break
    
cap.release()
cv2.destroyAllWindows()