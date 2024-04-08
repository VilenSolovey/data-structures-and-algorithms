import unittest
from find_num_of_islands import count_number_of_islands

class TestFindIslandsAmount(unittest.TestCase):
     
    @staticmethod
    def read_output_txt_files(self, output_file_path):
        with open(output_file_path, 'r') as file:
            return int(file.read().strip())

    def test_from_file1(self):
        count_number_of_islands('resources/input.txt', 'resources/output.txt')
        actual_result = self.read_output_txt_files('resources/output.txt')
        self.assertEqual(actual_result,2)

    def test_from_file2(self):
        count_number_of_islands('resources/input1.txt', 'resources/output1.txt')
        actual_result = self.read_output_txt_files('resources/output1.txt')
        self.assertEqual(actual_result,4)

    def test_from_file3(self):
        count_number_of_islands('resources/input2.txt', 'resources/output2.txt')
        actual_result = self.read_output_txt_files('resources/output2.txt')
        self.assertEqual(actual_result,3)

if __name__ == '__main__':
    unittest.main()
