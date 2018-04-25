# -*- coding: utf-8 -*-

"""
Ashley Wu
204612415
HW_9F
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

count=0

hip=cv2.imread('hip.png',0)
w,h=hip.shape[::-1]
x=np.ones(210)
y=np.ones(210)
cap=cv2.VideoCapture('RyanRun.mp4')

while (cap.isOpened()):

    if cap.grab():
        count=count+1
        if (872<=count<1082):
            flag, frame=cap.retrieve()
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
            img=frame.copy()
            res=cv2.matchTemplate(img,hip,cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(res)
            top_left=max_loc
            bottom_right=(top_left[0]+w,top_left[1]+h)
            cv2.rectangle(img,top_left,bottom_right,255,2)
    
            if top_left[1]--1*y[count-872-1]<100:
                x[count-872]=top_left[0]
                y[count-872]=-1*top_left[1]
            else:
                x[count-872]=x[count-872-1]
                y[count-872]=y[count-872-1]
    
            cv2.imshow('HW_9F',img)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    

cap.release()
cv2.destroyAllWindows()


plt.plot(x,y)
plt.xlabel('X Pixel')
plt.ylabel('Y Pixel')









