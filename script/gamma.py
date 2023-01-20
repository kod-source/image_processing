import cv2
import numpy as np
import const

# 画像読込
img = cv2.imread(const.FILE_PATH)

# """
# **********************************************************
# 【ガンマ補正の公式】
#   Y = 255(X/255)**(1/γ)

# 【γの設定方法】
#   ・γ>1の場合：画像が明るくなる
#   ・γ<1の場合：画像が暗くなる
# **********************************************************
# """

# ガンマ変換用の数値準備
gamma = 3.0  # γ値を指定
img2gamma = np.zeros((256, 1), dtype=np.uint8)  # ガンマ変換初期値

# 公式適用
for i in range(256):
    img2gamma[i][0] = 255 * (float(i) / 255) ** (1.0 / gamma)

# 読込画像をガンマ変換
gamma_img = cv2.LUT(img, img2gamma)

cv2.imwrite("img/gamma_" + const.FILE_NAME, gamma_img)
