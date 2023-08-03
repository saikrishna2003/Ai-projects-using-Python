import cv2
img=cv2.imread("sample1.png")
#cv2.imshow("pantech logo",img)
#cv2.imwrite("PantechLogo.png",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#print(img.shape)
#print(img.size)
#print(img.dtype)


grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("greyimage.jpg",grayImg)
cv2.imshow("Original",img)
cv2.imshow("Grayimage",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()