import cv2
import numpy as np

cap = cv2.imread('Azul.jpeg')
capt = cv2.resize(cap, dsize=(480,680),interpolation=cv2.INTER_CUBIC)

hsv = cv2.cvtColor(capt, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([80,70,40])
upper_red = np.array([140,255,255])
    
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(capt,capt, mask= mask)

kernel = np.ones((15,15),np.float32)/255
smoothed = cv2.filter2D(res,-1,kernel)

blur = cv2.GaussianBlur(res,(15,15),0)

median = cv2.medianBlur(res,15)

bilateral = cv2.bilateralFilter(res,15,75,75)

cv2.imshow('cap',capt)
#cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('blur',blur)
cv2.imshow('median',median)
cv2.imshow('bilateral',bilateral)

    
cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
