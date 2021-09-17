import  cv2

img1 =cv2.imread("1.jpg")
img2 =cv2.imread("2.jpg")

diff =cv2.subtract(img1,img2)
gray =cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
creat, mask =cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
diff[mask != 255] = [0,0,255]

img1[mask != 255] = [0,0,255]
img2[mask != 255] = [0,0,255]

cv2.imwrite('1.jpg',img1)
cv2.imwrite('2.jpg',img2)
cv2.imwrite('diffff.jpg',diff)