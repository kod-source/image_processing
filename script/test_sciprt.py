# import function
# import cv2

# # fileName = '10k.jpg'
# fileName = 'contrast_10k.tif'

# # 線を引いた座標のリスト
# coordinate = []
# # 画像データの読み込み＆画像に線を引く
# img = function.input_image(fileName, coordinate)
# # cv2.imshow('window', img) 
# cv2.imwrite("img/test_" + fileName, img)

from fileinput import filename
import cv2
from IPython.display import Image, display
from ipywidgets import widgets

fileName = '10k.tif'
image = cv2.imread("img/" + fileName, cv2.IMREAD_COLOR)
if image is None:
    print('ファイルオープンエラー')
    exit(0)

alpha = 1.0 # コントラスト項目
beta = 100    # 明るさ項目

# 明るさ・コントラスト操作
res_image = cv2.convertScaleAbs(image,alpha = alpha,beta = beta)
cv2.imwrite("img/contrast_" + fileName, res_image)