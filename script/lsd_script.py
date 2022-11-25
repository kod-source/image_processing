import cv2
import numpy as np
from pylsd.lsd import lsd
import matplotlib.pyplot as plt

def minusIntToPlus(i):
    if i > 0:
        return i
    return i * -1

fileName = '10k.jpg'
 
src = cv2.imread("img/" + fileName)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
 
lines = lsd(gray)
x = []
for i in range(lines.shape[0]):
    pt1 = (int(lines[i, 0]), int(lines[i, 1]))
    pt2 = (int(lines[i, 2]), int(lines[i, 3]))
    # x軸の値が等しいとき（横に平行）
    if pt1[1] == pt2[1]:
        i = pt1[0] - pt2[0] 
        x.append(minusIntToPlus(i))
        # cv2.line(src, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    elif pt1[0] == pt2[0]:
        i = pt1[1] - pt2[1] 
        x.append(minusIntToPlus(i))
    width = lines[i, 4]
    cv2.line(src, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    
cv2.imwrite("result/line_" + fileName, src)


# x = np.random.normal(60, 5, 500)
# print(x)
plt.hist(x, bins=200, range=(0, 80))
plt.show()


