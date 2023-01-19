import cv2
import numpy as np

fileName = "10k.tif"


def imshow(img):
    """ndarray 配列をインラインで Notebook 上に表示する。"""
    ret, encoded = cv2.imencode(".tif", img)
    display(Image(encoded))


def adjust(img, alpha=1.0, beta=0.0):
    # 積和演算を行う。
    dst = alpha * img + beta
    # [0, 255] でクリップし、uint8 型にする。
    return np.clip(dst, 0, 255).astype(np.uint8)


# 画像を読み込む。
src = cv2.imread("img/" + fileName)
# src = cv2.imread("calendar.png")
cv2.imshow("before", src)

# コントラスト、明るさを変更する。
dst = adjust(src, alpha=1.2, beta=30.0)
cv2.imshow("after", dst)
cv2.imwrite("img/contrast_" + fileName, dst)
cv2.waitKey(0)
