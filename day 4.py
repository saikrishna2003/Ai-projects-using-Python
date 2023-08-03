import cv2
import imutils
img=cv2.imread("sample1.png")
resizeimg=imutils.resize(img,width=20)
cv2.imwrite("resizedimage.jpg", resizeimg)