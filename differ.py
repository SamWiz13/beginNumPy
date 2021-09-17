import cv2
import  numpy as np

img1 =cv2.imread('1.jpg')
img2 =cv2.imread('2.jpg')

cv2.imshow("Img",img1)
cv2.waitKey(0)

cv2.imshow("Img",img2)
cv2.waitKey(0)

show =img2 -img1
show[show < 40] =255
cv2.imshow("Differnce",show)
cv2.waitKey(0)



