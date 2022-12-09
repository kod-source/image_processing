import cv2
import numpy as np
from pylsd.lsd import lsd


# 画像の読み込み＆画像に線を引く処理 (横の線を取得)
def input_image(file_name, coordinate):
    coordinate.clear()
    img = cv2.imread("img/" + file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lines = lsd(gray)
    # 画像に線を引く処理
    for i in range(lines.shape[0]):
        pt1 = (int(lines[i, 0]), int(lines[i, 1]))
        pt2 = (int(lines[i, 2]), int(lines[i, 3]))
        # x軸の値が等しいとき（横に平行）
        if pt1[1] == pt2[1]:
            coordinate.append(pt1)
            coordinate.append(pt2)
            width = lines[i, 4]
            cv2.line(img, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    return img

# 画像の読み込み＆画像に線を引く処理 (縦の線を取得)
def input_image_vertical(file_name, coordinate):
    coordinate.clear()
    img = cv2.imread("img/" + file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lines = lsd(gray)
    # 画像に線を引く処理
    for i in range(lines.shape[0]):
        pt1 = (int(lines[i, 0]), int(lines[i, 1]))
        pt2 = (int(lines[i, 2]), int(lines[i, 3]))
        # y軸の値が等しいとき（横に平行）
        if pt1[0] == pt2[0]:
            coordinate.append(pt1)
            coordinate.append(pt2)
            width = lines[i, 4]
            cv2.line(img, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    return img

# 画像の読み込み＆画像に線を引く処理 (全ての線を取得)
def input_all_image(file_name, coordinate):
    coordinate.clear()
    img = cv2.imread("img/" + file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lines = lsd(gray)
    # 画像に線を引く処理
    for i in range(lines.shape[0]):
        pt1 = (int(lines[i, 0]), int(lines[i, 1]))
        pt2 = (int(lines[i, 2]), int(lines[i, 3]))
        coordinate.append(pt1)
        coordinate.append(pt2)
        width = lines[i, 4]
        cv2.line(img, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    return img

# マイナスの値をプラスの値に変換
def minus_int_to_plus(i):
    if i > 0:
        return i
    return i * -1

# 長さから倍率を測定する
def diameter_calculate(l):
    result = 10000 * (6.29 / 463) * l
    return round(result, 2)

# 誤差率を計算する ((測定値 - 真値) ÷ 真値) × 100 [%]
def calculation_diff(theory, value):
    return round(((value - theory) / theory) * 100, 3)
