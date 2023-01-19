import unittest
import cv2
import numpy as np
import function


class TestShowAverage(unittest.TestCase):
    def test_show_average_with_valid_input(self):
        img = cv2.imread(file_path)
        results = [1, 2, 3, 4, 5]
        function.show_average(img, results)
        average = function.calculation_average(results)
        pos_average_str = "(average)=(" + str(average) + ")"
        (w, h), baseline = cv2.getTextSize(pos_average_str, cv2.FONT_HERSHEY_PLAIN, 2, 2)
        self.assertEqual((w, h), (252, 19))
        self.assertEqual(baseline, 11)

    def test_calculation_average_with_valid_input(self):
        results = [1, 2, 3, 4, 5]
        self.assertEqual(function.calculation_average(results), 3.0)


# 平均値を求めるテストコード
class TestCalculationAverage(unittest.TestCase):
    def test_calculation_average(self):
        # Test with a list of integers
        results = [1, 2, 3, 4, 5]
        self.assertEqual(function.calculation_average(results), 3.0)

        # Test with a list of floating point numbers
        results = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(function.calculation_average(results), 3.3)

        # Test with empty list
        results = []
        self.assertIsNone(function.calculation_average(results))

        # Test with a list of length 1
        results = [5]
        self.assertIsNone(function.calculation_average(results))


# 標準偏差を求めるテストコード
class TestCalculationStandardDeviation(unittest.TestCase):
    def test_calculation_standard_deviation(self):
        # Test with a list of integers
        results = [1, 2, 3, 4, 5]
        self.assertEqual(function.calculation_standard_deviation(results), 1.58)

        # Test with a list of floating point numbers
        results = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(function.calculation_standard_deviation(results), 1.74)

        # Test with empty list
        results = []
        self.assertIsNone(function.calculation_standard_deviation(results))

        # Test with a list of length 1
        results = [5]
        self.assertIsNone(function.calculation_standard_deviation(results))


# 倍率を測定するテストコード
class TestDiameterCalculate(unittest.TestCase):
    def test_diameter_calculate(self):
        # Test with value of l = 73.2
        l = 73.2
        self.assertEqual(function.diameter_calculate(l), 9944.45)

        # Test with value of l = 10
        l = 10
        self.assertEqual(function.diameter_calculate(l), 1358.53)

        # Test with value of l = 0
        l = 0
        self.assertEqual(function.diameter_calculate(l), 0)

        # Test with negative value of l
        l = -10
        self.assertEqual(function.diameter_calculate(l), -1358.53)


# マイナスの値をプラスの値に変換のテストコード
class TestMinusIntToPlus(unittest.TestCase):
    def test_minus_int_to_plus(self):
        # Test with positive value
        i = 10
        self.assertEqual(function.minus_int_to_plus(i), 10)

        # Test with negative value
        i = -10
        self.assertEqual(function.minus_int_to_plus(i), 10)

        # Test with zero
        i = 0
        self.assertEqual(function.minus_int_to_plus(i), 0)


class TestBrightnessAdjustment(unittest.TestCase):
    def test_brightness_adjustment(self):
        # Create an image with a gradient of pixel values
        gray_img = cv2.imread(file_path, 0)

        # Test the function
        new_img = function.brightness_adjustment(gray_img)
        # Check that the maximum value of the new image is less than or equal to 255
        self.assertLessEqual(np.max(new_img), 255)
        # Check that the minimum value of the new image is greater than or equal to 0
        self.assertGreaterEqual(np.min(new_img), 0)


class TestInputImage(unittest.TestCase):
    def test_input_image(self):
        # Create an image with a gradient of pixel values
        gray_img = cv2.imread(file_path, 0)
        # define the list to store the coordinates
        coordinates = []
        # Test the function
        function.input_image(gray_img, coordinates)
        # check if the line segment is acquired.
        self.assertNotEqual(len(coordinates), 0)


class TestInputImageVertical(unittest.TestCase):
    def test_input_image_vertical(self):
        # Create an image with a gradient of pixel values
        gray_img = cv2.imread(file_path, 0)
        # define the list to store the coordinates
        coordinates = []
        # Test the function
        function.input_image_vertical(gray_img, coordinates)
        # check if the line segment is acquired.
        self.assertNotEqual(len(coordinates), 0)


class TestInputImageAll(unittest.TestCase):
    def test_input_image_all(self):
        # Create an image with a gradient of pixel values
        gray_img = cv2.imread(file_path, 0)
        # define the list to store the coordinates
        coordinates = []
        # Test the function
        function.input_all_image(gray_img, coordinates)
        # check if the line segment is acquired.
        self.assertNotEqual(len(coordinates), 0)


if __name__ == "__main__":
    file_path = "img/test_10k.jpg"
    unittest.main()
