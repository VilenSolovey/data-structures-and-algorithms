import math


def find_wire_length(distance, previous_pillar, current_pillar):
    """
    In this function we find the wire length between two pillars

    Args:
        distance (int): The  distance between the pillars.
        previous_pillar (int): The height of the previous pillar that we consider in cycle
        current_pillar (int): The height of the current pillar that we consider in cycle

    Returns:
        float: The length of the wire needed to connect the two pillars
    """
    return math.sqrt(distance ** 2 + (previous_pillar - current_pillar) ** 2)


def maximum_wire_length(distance, heights, output_filename):
    """
    This function find the maximum wire length needed to connect all the pillars
    And of course write the result in output file

    Args:
        distance (int): The horizontal distance between consecutive pillars
        heights (list of int): The list of maximum heights for each pillar
        output_filename (str): The name of the file to write the result

    Returns:
        float: The maximum length of wire
    """
    amount_of_pillars = len(heights)

    value_bottom = 0
    value_top = 0

    for pillar in range(1, amount_of_pillars):
        
        previous_bottom_to_current_bottom = value_bottom + find_wire_length(distance, 1, 1)
        preevious_top_to_current_bottom = value_top + find_wire_length(distance, 1, heights[pillar - 1])
        current_value_bottom = max(previous_bottom_to_current_bottom, preevious_top_to_current_bottom)
        previous_bottom_to_current_top = value_bottom + find_wire_length(distance, heights[pillar], 1)
        previous_top_to_current_top = value_top + find_wire_length(distance, heights[pillar], heights[pillar - 1])
        current_value_top = max(previous_bottom_to_current_top, previous_top_to_current_top)

        value_bottom = current_value_bottom
        value_top = current_value_top

    wire_lenght = round(max(value_top, value_bottom), 2)

    with open(output_filename, 'w') as file:
        file.write(f"{wire_lenght}") 

    return wire_lenght


def read_input(filename):
    """
    This function read input data from a file that are in the folder resources

    Args:
        filename (str): This is the name of the input file

    Returns:
        tuple: A tuple containing: the distance between pillars and a list of heights.
    """
    with open(filename, 'r') as file:
        distance = int(file.readline().strip())
        heights = list(map(int, file.readline().strip().split()))

    return distance, heights
