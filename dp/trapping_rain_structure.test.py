from trapping_rain_structure import get_water_volume
import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arr = [0, 1]
        self.assertEqual(get_water_volume(arr), 0)

    def test_case_2(self):
        arr = [0, 1, 0]
        self.assertEqual(get_water_volume(arr), 0)

    def test_case_3(self):
        arr = [1, 0, 1]
        self.assertEqual(get_water_volume(arr), 1)

    def test_case_4(self):
        arr = [2, 0, 1]
        self.assertEqual(get_water_volume(arr), 1)

    def test_case_5(self):
        arr = [2, 0, 2]
        self.assertEqual(get_water_volume(arr), 2)

    def test_case_6(self):
        arr = [2, 0, 3]
        self.assertEqual(get_water_volume(arr), 2)

    def test_case_6(self):
        arr = [2, 0, 3, 0]
        self.assertEqual(get_water_volume(arr), 2)

    def test_case_7(self):
        arr = [2, 0, 3, 0, 1]
        self.assertEqual(get_water_volume(arr), 3)

    def test_case_8(self):
        arr = [4,2,0,3,2,5]
        self.assertEqual(get_water_volume(arr), 9)

    def test_case_9(self):
        arr = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(get_water_volume(arr), 6)

if __name__ == '__main__':
    unittest.main()