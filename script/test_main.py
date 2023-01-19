import unittest
import cv2
import numpy as np
import os
import main

# 必要なパラメータを定義するテストコード
class TestDefineParams(unittest.TestCase):
    def test_define_params(self):
        # create a test image
        test_img = np.ones((100, 100, 3), np.uint8) * 255
        cv2.imwrite("example.png", test_img)

        # test the function with is_vertical=True
        params = main.define_params(True)
        self.assertEqual(params["is_vertical"], True)
        self.assertEqual(params["img"].shape, (100, 100, 3))
        self.assertEqual(len(params["coordinates"]), 0)
        self.assertEqual(len(params["show_result_coordinates"]), 0)
        self.assertEqual(len(params["diameter_results"]), 0)

        # test the function with is_vertical=False
        params = main.define_params(False)
        self.assertEqual(params["is_vertical"], False)
        self.assertEqual(params["img"].shape, (100, 100, 3))
        self.assertEqual(len(params["coordinates"]), 0)
        self.assertEqual(len(params["show_result_coordinates"]), 0)
        self.assertEqual(len(params["diameter_results"]), 0)

        # remove the test image
        os.remove("example.png")

    def test_define_params_no_file(self):
        # test the function and check if the expected exception is raised
        with self.assertRaises(FileNotFoundError):
            main.define_params(True)


class TestFilterCoordinatesByPosition(unittest.TestCase):
    def test_filter_coordinates_by_position(self):
        coordinates = [
            (100, 100),
            (105, 105),
            (110, 110),
            (115, 115),
            (120, 120),
        ]
        x = 105
        y = 108
        expected = [(105, 105), (110, 110)]
        result = main.filter_coordinates_by_position(x, y, coordinates)
        self.assertEqual(result, expected)

    def test_filter_coordinates_by_position_no_result(self):
        coordinates = [
            (100, 100),
            (105, 105),
            (110, 110),
            (115, 115),
            (120, 120),
        ]
        x = 150
        y = 150
        expected = []
        result = main.filter_coordinates_by_position(x, y, coordinates)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main.const.FILE_PATH = "example.png"
    unittest.main()
