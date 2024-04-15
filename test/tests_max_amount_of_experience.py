import unittest
from max_amount_of_experience import calculate_max_experience


def read_input_from_file(filename):
    with open(filename, 'r') as file:
        num_levels = int(file.readline())
        pyramid = []

        for i in range(num_levels):
            level = list(map(int, file.readline().split()))
            pyramid.append(level)
    return pyramid


class TestMaxExperience(unittest.TestCase):
    def test_first_calculate_max_experience(self):
        input_filename = 'resources_lab6/career_in1.txt'
        company_structure = read_input_from_file(input_filename)

        output_filename = 'resources_lab6/career.out1.txt'

        calculate_max_experience(company_structure, 'resources_lab6/career.out1.txt')

        with open(output_filename, 'r') as file:
            result = int(file.readline())

        self.assertEqual(result, 12)

    def test_second_calculate_max_experience(self):
        input_filename = 'resources_lab6/career_in2.txt'
        company_structure = read_input_from_file(input_filename)

        output_filename = 'resources_lab6/career.out2.txt'

        calculate_max_experience(company_structure, 'resources_lab6/career.out2.txt')

        with open(output_filename, 'r') as file:
            result = int(file.readline())

        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
