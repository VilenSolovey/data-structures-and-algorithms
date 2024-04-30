import unittest
from src.find_min_cable_length import prim_algorithm_for_iot


class TestPrimAlgorithm(unittest.TestCase):
    @staticmethod
    def read_edges_and_nodes_from_file(file_path):
        vertices = []
        node_set = set()
        with open(file_path, 'r') as file:
            for line in file:
                first_vertex, second_vertex, weight = line.strip().split(',')
                first_vertex, second_vertex, weight = int(first_vertex), int(second_vertex), int(weight)
                vertices.append((first_vertex, second_vertex, weight))
                node_set.update([first_vertex, second_vertex])
        amount_of_vertices = max(node_set) + 1
        return vertices, amount_of_vertices

    def test_search_of_length_1(self):
        file_path = "resources/resources_lab8/communication_wells.csv"
        vertices, amount_of_vertices = self.read_edges_and_nodes_from_file(file_path)
        find_cable_length = prim_algorithm_for_iot(vertices, amount_of_vertices)
        self.assertEqual(29, find_cable_length)

    def test_search_of_length_2(self):
        file_path = "resources/resources_lab8/communication_wells_2.csv"
        vertices, amount_of_vertices = self.read_edges_and_nodes_from_file(file_path)
        find_cable_length = prim_algorithm_for_iot(vertices, amount_of_vertices)
        self.assertEqual(45, find_cable_length)


if __name__ == '__main__':
    unittest.main()
