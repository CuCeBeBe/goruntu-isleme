#Mislina Mihriban Yılmaz 02200201025 3. sınıf örgün
import cv2
import numpy as np

photo=cv2.imread("resim.png",0)
cv2.imshow("duzresim",photo)
cv2.waitKey()

max_photo=np.max(photo)

[h,w]=np.shape(photo)

for i in range (0,h):
    for j in range (0,w):
        photo[i,j]=max_photo-photo[i,j]

cv2.imshow("tersresim",photo)
cv2.waitKey()
