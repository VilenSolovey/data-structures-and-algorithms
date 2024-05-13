import unittest
from src.find_min_board_size import find_min_board_size


class TestLab1(unittest.TestCase):
    def test_find_min_board_size1(self):
        self.assertEqual(find_min_board_size(10, 2, 3),9)

    def test_find_min_board_size2(self):
        self.assertEqual(find_min_board_size(4, 1, 1),2)

    def test_find_min_board_size3(self):
        self.assertEqual(find_min_board_size(2, 1000000000, 999999999),1999999998)


if __name__ == '__main__':
    unittest.main()
