import unittest
from src.find_if_arr_is_monotonic import is_arr_monotonic


class TestLab1(unittest.TestCase):
    def test_one_element_arr(self):
        self.assertTrue(is_arr_monotonic([1]))

    def test_increasing(self):
        self.assertTrue(is_arr_monotonic([1, 2, 2, 10, 15]))

    def test_decreasing(self):
        self.assertTrue(is_arr_monotonic([10, 6, 4, 2, 1]))

    def test_non_monotonic(self):
        self.assertFalse(is_arr_monotonic([1, 5, 6, 7, 2, 3, 4, 5]))

    def test_null_array(self):
        self.assertTrue(is_arr_monotonic([]))

    def test_for_correctness1(self):
        self.assertTrue(is_arr_monotonic([2, 2, 2, 2, 1]))

    def test_for_correctness2(self):
        self.assertTrue(is_arr_monotonic([3, 3, 3, 3, 3]))

    def test_for_correctness3(self):
        self.assertTrue(is_arr_monotonic([3, 3, 3, 3, 5]))


if __name__ == '__main__':
    unittest.main()
