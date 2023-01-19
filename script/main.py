import os
import cv2
import function
import const

def main():
    is_vertical = False
    params = define_params(is_vertical)
    output(params)

def define_params(is_vertical):
    if not os.path.isfile(const.FILE_PATH):
        raise FileNotFoundError('Image file not found!')
    gray_img = cv2.imread(const.FILE_PATH, 0)
    # 線を引いた座標のリスト
    coordinates = []
    # 画像の輝度の自動調整
    gray_brightness_adjustment_img = function.brightness_adjustment(gray_img)
    # 画像に線を引く
    img = function.input_image_vertical(gray_brightness_adjustment_img, coordinates) if is_vertical else function.input_image(gray_brightness_adjustment_img, coordinates)
    # 計算結果を求めるための必要な座標のリスト
    show_result_coordinates = []
    # 全ての倍率結果の値のリスト
    diameter_results = []

    params = {
        "img": img,
        "coordinates": coordinates,
        "show_result_coordinates": show_result_coordinates,
        "diameter_results": diameter_results,
        "is_vertical": is_vertical,
    }
    return params

def filter_coordinates_by_position(x, y, coordinates):
    # x軸で曖昧検索でfilterする
    filter_coordinates = []
    for list in coordinates:
        if int(x) - 5 <= list[0] <= int(x) + 5:
            filter_coordinates.append(list)
    # y軸で曖昧検索でfilterする
    new_filter_coordinates = []
    for list in filter_coordinates:
        if int(y) - 5 <= list[1] <= int(y) + 5:
            new_filter_coordinates.append(list)
    return new_filter_coordinates

def show_image(show_img, x, y, params):
    global count
    # クリックした位置で座標が存在するか確認する
    filter_coordinates = filter_coordinates_by_position(x, y, params["coordinates"])

    # 条件にヒットする座標が複数ある時は処理を終了
    if len(filter_coordinates) != 1:
        return
    params["show_result_coordinates"].append(filter_coordinates[0])

    # クリックした座標を表示する
    cv2.circle(show_img, center=(filter_coordinates[0][0], filter_coordinates[0][1]), radius=5, color=255, thickness=-1)
    pos_str=''+str(count)+'(x,y)=('+str(filter_coordinates[0][0])+','+str(filter_coordinates[0][1])+')'
    cv2.putText(show_img, pos_str, (filter_coordinates[0][0]+10, filter_coordinates[0][1]+10), cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)

    # 計算結果の表示（答え）
    length = len(params["show_result_coordinates"])
    if length > 0 and length % 2 == 0:
        x_shaft = 1600
        y_shaft = 200 + length * 40
        var = 0 if params["is_vertical"] else 1
        l = function.minus_int_to_plus(params["show_result_coordinates"][length-2][var] - params["show_result_coordinates"][length-1][var])
        result = function.diameter_calculate(l)
        diff = function.calculation_diff(const.DESIRED_VALUE, result)
        params["diameter_results"].append(result)
        pos_result_str='(result'+str(count)+')=('+str(result)+')'
        pos_diff_str='(diff'+str(count)+')=('+str(diff)+')'
        count += 1
        cv2.putText(show_img,pos_result_str,(x_shaft, y_shaft),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)
        cv2.putText(show_img,pos_diff_str,(x_shaft, y_shaft + 35),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)
    cv2.imshow('window', show_img)

# クリックしたら座標の位置を表示する処理
def click_pos(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        show_image(params["img"], x, y, params)

def output(params):
    cv2.namedWindow('window', cv2.WINDOW_NORMAL)
    cv2.imshow('window', params["img"])
    cv2.setMouseCallback('window', click_pos, params)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 処理が終了したら平均値と標準偏差を表示する
    function.show_average(params["img"], params["diameter_results"])
    function.show_standard_deviation(params["img"], params["diameter_results"])
    result_name = "result/click_vertical_" if params["is_vertical"] else "result/click_"
    cv2.imwrite(result_name + const.FILE_NAME, params["img"])

if __name__ == '__main__':
    # 何回目かを示すための値
    count = 1
    main()
