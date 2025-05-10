#basic utility function-1
import cv2
import numpy as np
img1=cv2.imread("starbg.jpg")
img2=cv2.imread("clpsdbuilding.jpg")
q=cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow("BG merging",q)
cv2.waitKey(0)
e=cv2.subtract(img1,img2)
cv2.imshow("idk",e)
cv2.waitKey(0)
resized=cv2.resize(img2,(100,100))
cv2.imshow("resize",resized)
cv2.waitKey(0)

#kernel is used for erosion as an input
w=cv2.imread("pikachu.png")
k=np.ones((3,3),np.uint8)
r=cv2.erode(w,k)

cv2.imshow("...",r)
cv2.waitKey(0)

#blurring of an image
#Gaussian Blur - used mostly in machine preprocessing steps
G= cv2.GaussianBlur(w,(11,11),sigmaX=0)
cv2.imshow("Gausssian",G)
cv2.waitKey(0)

cv2.destroyAllWindows()  