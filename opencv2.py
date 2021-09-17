import cv2
import numpy as np

im = cv2.imread("./1.jpg")
im =np.rot90(im,2)
cv2.imshow("image", im)
cv2.waitKey(0)