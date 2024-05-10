"""Lab 8"""
from src.heap_based_priority_queue import BinaryHeap


def create_graph(edges, num_nodes):
    """
    Function to create a graph using an adjacency list.
    Args:
        edges (list of tuples): List of tuples (first_vertex, second_vertex, weight),
        num_nodes (int): Number of vertices in the graph.

    Returns:
        list: Adjacency list for each vertex.
    """
    input_graph = []
    for i in range(num_nodes):
        input_graph.append([])

    for first_vertex, second_vertex, weight in edges:
        input_graph[first_vertex].append([second_vertex, weight])
        input_graph[second_vertex].append([first_vertex, weight])
    return input_graph


def prim_algorithm_for_iot(vertices, amount_of_vertices):
    """
    Direct implementation of Prims algorithm for finding MST with using max BinaryHeap

    Args:
        vertices (list of tuples): List of graph edges, where each tuple = (first_vertex, second_vertex, weight).
        amount_of_vertices (int): Total number of vertices taken from the file

    Returns:
        int: cable_length
    """
    first_vertex, cable_length, count_of_vertices = 0, 0, 0
    prima_graph = create_graph(vertices, amount_of_vertices)
    priority_queue = BinaryHeap()
    visited = set()
    visited.add(first_vertex)

    # Add all vertices adjacent to the first vertex to the priority queue with negative weight
    # We implement through negative value, because of max BinaryHeap
    for next_vertex, distance in prima_graph[first_vertex]:
        priority_queue.add_element((first_vertex, next_vertex), -distance)

    while priority_queue.queue:
        vertex = priority_queue.pop_elem()
        (from_vertex, vertex), negative_distance = vertex
        # Convert weight to positive for correct algorithm implementation
        distance = -negative_distance

        if vertex not in visited:
            visited.add(vertex)
            cable_length += distance
            count_of_vertices += 1
            # Adding neighboring vertices of the current vertex that have not yet been visited
            for neighbour_vertex, neighbour_distance in prima_graph[vertex]:
                if neighbour_vertex not in visited:
                    priority_queue.add_element((vertex, neighbour_vertex), -neighbour_distance)

    # Check if there is a vertex that is not connected to the graph
    if count_of_vertices != amount_of_vertices - 1:
        return -1
    return cable_length
