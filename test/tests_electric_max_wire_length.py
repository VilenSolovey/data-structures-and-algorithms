import unittest
from src.electric_max_wire_length import read_input, maximum_wire_length


class TestMaxWireLength(unittest.TestCase):

    def test_electricity_case_1(self):
        distance, heights = read_input('test/resources/resources_lab9/electricians_in1.txt')
        output_length = maximum_wire_length(distance, heights, 'test/resources/resources_lab9/electricians_out1.txt')
        self.assertEqual(output_length, 5.66)

    def test_electricity_case_2(self):
        distance, heights = read_input('test/resources/resources_lab9/electricians_in2.txt')
        output_length = maximum_wire_length(distance, heights, 'test/resources/resources_lab9/electricians_out2.txt')
        self.assertEqual(output_length, 396.32)

    def test_electricity_case_3(self):
        distance, heights = read_input('test/resources/resources_lab9/electricians_in3.txt')
        output_length = maximum_wire_length(distance, heights, 'test/resources/resources_lab9/electricians_out3.txt')
        self.assertEqual(output_length, 2738.18)


if __name__ == '__main__':
    unittest.main()
