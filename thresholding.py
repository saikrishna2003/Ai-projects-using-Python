import cv2
img=cv2.imread("sample1.png")
grayscaling=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshimg=cv2.threshold(grayscaling, 120, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholding.jpg",threshimg)