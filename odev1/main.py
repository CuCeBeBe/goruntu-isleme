import cv2
import numpy as np

resim=cv2.imread("gri.jpg",0) # fotoğrafı alma
cv2.imshow("gri",resim) # fotoğrafı gösterme
cv2.waitKey() # kapatana kadar gösterme
hist= np.zeros(256)
[h,w]=np.shape(resim)
for i in range (0,h): # piksellere göre değer atama
    for j in range (0,w):
        k=resim[i,j]
        hist[k]=hist[k]+1
for m in range (0,256): # histogram dizisini bastırma
    print(m,"-->",hist[m])
