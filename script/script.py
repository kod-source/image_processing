# ライブラリインポート
import cv2
import numpy as np

# 画像の解像度を指定
pixel = 0.178  # mm/pixel
# 長さを測る高さを指定
analysis_row = 360
# 画像の読み込み
picgray = cv2.imread("line_10k.jpg", cv2.IMREAD_GRAYSCALE)
# 二値化データの作成
ret, thresh = cv2.threshold(picgray, 5, 255, cv2.THRESH_BINARY)
# 輪郭抽出
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
max_cnt = max(contours, key=lambda x: cv2.contourArea(x))
# 輪郭内を塗りつぶし
pic_thresh = cv2.drawContours(picgray, [max_cnt], -1, 255, -1)
# 指定行のデータを週出
bright_data = pic_thresh[analysis_row, :]
# 長さを算出
num_pix = np.count_nonzero(bright_data)
length = round(num_pix)
print(str(length))
