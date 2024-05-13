import unittest
from src.sum_of_tree_depths import sum_of_depths, TreeNode


class TestSumOfDepths(unittest.TestCase):
    def test_none_tree(self):
        root = None
        self.assertEqual(sum_of_depths(root), 0)

    def test_one_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test_simple_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        self.assertEqual(sum_of_depths(root), 2)

    def test_big_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(6)
        self.assertEqual(sum_of_depths(root), 9)

if __name__ == '__main__':
    unittest.main()
