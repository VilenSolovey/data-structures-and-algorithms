import unittest
from finding_indices_of_occurrences_with_KMP import knuth_morris_pratt


class MyTestCase(unittest.TestCase):
    def test_lab7_case1(self):
        self.assertEqual(knuth_morris_pratt('CD', 'CDCDCDCD'), {0, 2, 4, 6})

    def test_lab7_case2(self):
        self.assertEqual(knuth_morris_pratt('Vilen', 'Vilen in the London, Vilen'), {0, 21})

    def test_lab7_case3(self):
        self.assertEqual(knuth_morris_pratt('ADC', 'BADCDADC'), {1, 5})

    def test_lab7_case4(self):
        self.assertEqual(knuth_morris_pratt('ADCADCCA', 'BADCADCDDADCADCADCCACCA'), {12})


if __name__ == '__main__':
    unittest.main()
