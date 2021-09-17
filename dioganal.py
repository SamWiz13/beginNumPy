import cv2
import  numpy as np

img =np.full((255,255,3),0,dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.line(img,(0,0),(255,255),(255,255,255),1)
cv2.line(img,(255,0),(0,255),(255,255,255),1)
cv2.imshow("Image", img)
cv2.waitKey(0)