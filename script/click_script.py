import os
import cv2
import function

file_name = '10k.jpg'
file_path = "img/" + file_name
if not os.path.isfile(file_path):
    raise FileNotFoundError('Image file not found!')
gray_img = cv2.imread(file_path, 0)

# 希望値（誤差率の計算で使用）
desired_value = 10000
# 線を引いた座標のリスト
coordinate = []
# 画像の輝度の自動調整
gray_brightness_adjustment_img = function.brightness_adjustment(gray_img)
# 画像に線を引く
img = function.input_image(gray_brightness_adjustment_img, coordinate)
# 計算結果を求めるための必要な座標のリスト
show_result_coordinates = []
# 何回目かを示すための値
count = 1
# 全ての倍率結果の値のリスト
diameter_results = []

def show_image(show_img, x, y):
    global count
    # x軸で曖昧検索でfilterする
    filter_coordinate = []
    for list in coordinate:
        if int(x) - 5 <= list[0] <= int(x) + 5:
            filter_coordinate.append(list)
    # y軸で曖昧検索でfilterする
    new_filter_coordinate = []
    for list in filter_coordinate:
        if int(y) - 5 <= list[1] <= int(y) + 5:
            new_filter_coordinate.append(list)

    # 条件にヒットする座標が複数ある時は処理を終了
    if len(new_filter_coordinate) != 1:
        return
    show_result_coordinates.append(new_filter_coordinate[0])

    # クリックした座標を表示する
    cv2.circle(show_img, center=(new_filter_coordinate[0][0], new_filter_coordinate[0][1]), radius=5, color=255, thickness=-1)
    pos_str=''+str(count)+'(x,y)=('+str(new_filter_coordinate[0][0])+','+str(new_filter_coordinate[0][1])+')'
    cv2.putText(show_img, pos_str, (new_filter_coordinate[0][0]+10, new_filter_coordinate[0][1]+10), cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)

    # 計算結果の表示（答え）
    length = len(show_result_coordinates)
    if length > 0 and length % 2 == 0:
        x_shaft = 1600
        y_shaft = 200 + length * 40
        l = function.minus_int_to_plus(show_result_coordinates[length-2][1] - show_result_coordinates[length-1][1])
        result = function.diameter_calculate(l)
        diff = function.calculation_diff(desired_value, result)
        diameter_results.append(result)
        pos_result_str='(result'+str(count)+')=('+str(result)+')'
        pos_diff_str='(diff'+str(count)+')=('+str(diff)+')'
        count += 1
        cv2.putText(show_img,pos_result_str,(x_shaft, y_shaft),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)
        cv2.putText(show_img,pos_diff_str,(x_shaft, y_shaft + 35),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)
    cv2.imshow('window', show_img)

# クリックしたら座標の位置を表示する処理
def click_pos(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        show_image(img, x, y)

cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.imshow('window', img)
cv2.setMouseCallback('window', click_pos)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 処理が終了したら平均値を表示する
function.show_average(img, diameter_results)
cv2.imwrite("result/click_" + file_name, img)
