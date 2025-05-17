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

#median blur-used in digital processing preserves edges but removes noise
m= cv2.medianBlur(w,3)
cv2.imshow("median",m)
cv2.waitKey(0)

#bilateral blur - only sharp edges are preserved here
b= cv2.bilateralFilter(w,3,75,75)
cv2.imshow("bilateral",b)
cv2.waitKey(0)
#src − A Mat object representing the source (input image) for this operation.
'''dst − A Mat object representing the destination (output image) for this operation.
d − A variable of the type integer representing the diameter of the pixel neighborhood.
sigmaColor − A variable of the type integer representing the filter sigma in the color space.
sigmaSpace − A variable of the type integer representing the filter sigma in the coordinate space.
borderType − An integer object representing the type of the border used.'''
j=cv2.imread("ashborn.png")
borderimg=cv2.copyMakeBorder(j,100,100,100,100,cv2.BORDER_CONSTANT )
cv2.imshow("border image",borderimg)
cv2.waitKey(0)
cv2.destroyAllWindows()  
