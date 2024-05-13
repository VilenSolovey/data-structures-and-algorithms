import unittest
from src.heap_based_priority_queue import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    def test_add_and_peek(self):
        heap = BinaryHeap()
        heap.add_element(1, 1)
        heap.add_element(2, 2)
        self.assertEqual(heap.queue[0], (2, 2))

    def test_pop(self):
        heap = BinaryHeap()
        heap.add_element(1, 1)
        heap.add_element(2, 2)
        heap.add_element(3, 3)
        heap.pop_elem()
        self.assertNotIn((3, 3), heap.queue)


    def test_peek_empty(self):
        heap = BinaryHeap()
        self.assertIsNone(heap.peak_queue())


if __name__ == '__main__':
    unittest.main()
