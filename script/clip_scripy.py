import cv2
import numpy as np
from pylsd.lsd import lsd
import matplotlib.pyplot as plt

fileName = '10k.jpg'
 
src = cv2.imread("img/" + fileName)
img2 = src[800 : 1000, 1450: 1550]
cv2.imwrite("result/kitirori.jpg", img2)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
 
lines = lsd(gray)
x = []
for i in range(lines.shape[0]):
    pt1 = (int(lines[i, 0]), int(lines[i, 1]))
    pt2 = (int(lines[i, 2]), int(lines[i, 3]))
    if pt1[1] == pt2[1]: 
        print("pt1",  pt1) 
        print("pt2",  pt2) 
        width = lines[i, 4]
        cv2.line(img2, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    
cv2.imwrite("result/kiritori" + fileName, img2)
