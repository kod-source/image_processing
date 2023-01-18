import unittest
import cv2
import function

class TestShowAverage(unittest.TestCase):
    def test_show_average_with_valid_input(self):
        img = cv2.imread('test_image.jpg')
        results = [1, 2, 3, 4, 5]
        function.show_average(img, results)
        average = calculation_average(results)
        pos_average_str='(average)=('+str(average)+')'
        self.assertEqual(cv2.getTextSize(pos_average_str, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0], (246, 30))
        self.assertEqual(cv2.getTextSize(pos_average_str, cv2.FONT_HERSHEY_PLAIN, 2, 2)[1], 30)

    def test_show_average_with_invalid_input(self):
        img = cv2.imread('test_image.jpg')
        results = []
        function.show_average(img, results)
        self.assertEqual(cv2.getTextSize(pos_average_str, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0], None)
        self.assertEqual(cv2.getTextSize(pos_average_str, cv2.FONT_HERSHEY_PLAIN, 2, 2)[1], None)

    def test_calculation_average_with_valid_input(self):
        results = [1, 2, 3, 4, 5]
        self.assertEqual(calculation_average(results), 3.0)

if __name__ == '__main__':
    unittest.main()
