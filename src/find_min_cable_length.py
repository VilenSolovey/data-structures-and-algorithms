"""Lab 8"""
from src.heap_based_priority_queue import BinaryHeap


def create_graph(edges, num_nodes):
    input_graph = []
    for i in range(num_nodes):
        input_graph.append([])

    for first_vertex, second_vertex, weight in edges:
        input_graph[first_vertex].append([second_vertex, weight])
        input_graph[second_vertex].append([first_vertex, weight])
    return input_graph


def prim_algorithm_for_iot(vertices, amount_of_vertices):
    first_vertex, cable_length, count_of_vertices = 0, 0, 0
    prima_graph = create_graph(vertices, amount_of_vertices)
    priority_queue = BinaryHeap()
    visited = set()
    visited.add(first_vertex)

    for next_vertex, distance in prima_graph[first_vertex]:
        priority_queue.add_element((first_vertex, next_vertex), -distance)

    while priority_queue.queue:
        vertex = priority_queue.pop_elem()
        (from_vertex, vertex), negative_distance = vertex
        distance = -negative_distance

        if vertex not in visited:
            visited.add(vertex)
            cable_length += distance
            count_of_vertices += 1
            for neighbour_vertex, neighbour_distance in prima_graph[vertex]:
                if neighbour_vertex not in visited:
                    priority_queue.add_element((vertex, neighbour_vertex), -neighbour_distance)

    if count_of_vertices != amount_of_vertices - 1:
        return -1
    return cable_length
