import cv2
import numpy as np
import os
from pylsd.lsd import lsd
from statistics import stdev

# 画像に線を引く処理 (横の線を取得)
def input_image(gray_img, coordinates):
    img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
    coordinates.clear()
    lines = lsd(gray_img)
    # 画像に線を引く処理
    for i in range(lines.shape[0]):
        pt1 = (int(lines[i, 0]), int(lines[i, 1]))
        pt2 = (int(lines[i, 2]), int(lines[i, 3]))
        # y軸の値が等しいとき（横に平行）
        if pt1[1] == pt2[1]:
            coordinates.append(pt1)
            coordinates.append(pt2)
            width = lines[i, 4]
            cv2.line(img, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    return img

# 画像に線を引く処理 (縦の線を取得)
def input_image_vertical(gray_img, coordinates):
    img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
    coordinates.clear()
    lines = lsd(gray_img)
    # 画像に線を引く処理
    for i in range(lines.shape[0]):
        pt1 = (int(lines[i, 0]), int(lines[i, 1]))
        pt2 = (int(lines[i, 2]), int(lines[i, 3]))
        # x軸の値が等しいとき（縦に平行）
        if pt1[0] == pt2[0]:
            coordinates.append(pt1)
            coordinates.append(pt2)
            width = lines[i, 4]
            cv2.line(img, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    return img

# 画像の読み込み＆画像に線を引く処理 (全ての線を取得)
def input_all_image(gray_img, coordinates):
    img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
    coordinates.clear()
    lines = lsd(gray_img)
    # 画像に線を引く処理
    for i in range(lines.shape[0]):
        pt1 = (int(lines[i, 0]), int(lines[i, 1]))
        pt2 = (int(lines[i, 2]), int(lines[i, 3]))
        coordinates.append(pt1)
        coordinates.append(pt2)
        width = lines[i, 4]
        cv2.line(img, pt1, pt2, (0, 0, 255), int(np.ceil(width / 2)))
    return img

# 画像の拡張子をjpgに変更する
def change_extension(file_name):
    img = cv2.imread("img/" + file_name)
    # 拡張子を取り除くファイル名を取得する
    file_path = os.path.splitext(os.path.basename(file_name))[0]
    cv2.imwrite("img/" + file_path + ".jpg", img)

# ネガポシ変換 (色を反転する処理)
def conversion_negative_positive(file_name):
    img = cv2.imread("img/" + file_name)
    negative_img = cv2.bitwise_not(img)
    cv2.imwrite("img/negative" + file_name, negative_img)

# 画像の輝度自動調整
def brightness_adjustment(gray_img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    new_img = clahe.apply(gray_img)
    return new_img

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

# 平均値を求める
def calculation_average(results):
    return round(sum(results) / len(results), 2)

# 平均値を画像上に表示する
def show_average(img, results):
    if len(results) < 2:
        return
    average = calculation_average(results)
    pos_average_str='(average)=('+str(average)+')'
    cv2.putText(img,pos_average_str,(1600, 200),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)

# 標準偏差を求める
def calculation_standard_deviation(results):
    std = stdev(results)
    return round(std, 2)

# 標準偏差を画像上に表示する
def show_standard_deviation(img, results):
    if len(results) < 2:
        return
    standard_deviation = calculation_standard_deviation(results)
    pos_standard_deviation_str='(deviation)=('+str(standard_deviation)+')'
    cv2.putText(img,pos_standard_deviation_str,(1600, 235),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)
