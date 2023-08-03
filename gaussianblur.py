import cv2
img=cv2.imread("sample1.png")
gaussianblurimg=cv2.GaussianBlur(img, (21,21), 0)
cv2.imwrite("gaussianblur.jpg",gaussianblurimg)
