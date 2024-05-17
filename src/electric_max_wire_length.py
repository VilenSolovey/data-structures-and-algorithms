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

    # Creating an empty table where we keep the maximums wire length
    # by considering the current pillar height as either 1 or its maximum height
    cable_length = []
    for pillar in range(amount_of_pillars):
        cable_length.append([0, 0])

    # In this cycle, we go through heights from the second height to the end
    for pillar in range(1, amount_of_pillars):
        # Here we find the wire length in case when we consider the minimum height in the conditions it is 1
        # First, we try to find wire length from the bottom of the current pillar to the bottom of the previous pillar
        current_bottom_previous_bottom = cable_length[pillar - 1][0] + find_wire_length(distance, 1, 1)
        # Then, we try to find wire length from the top of the current pillar to the bottom of the previous pillar
        current_top_previous_top = cable_length[pillar - 1][1] + find_wire_length(distance, 1, heights[pillar - 1])
        cable_length[pillar][0] = max(current_bottom_previous_bottom, current_top_previous_top)
        # Here we find the wire length in case when we consider the maximum possible height of the pillar
        # First, we try to find wire length from the bottom of the current pillar to the top of the previous pillar
        current_bottom_previous_top = cable_length[pillar - 1][0] + find_wire_length(distance, heights[pillar], 1)
        # Then, we try to find wire length from the top of the current pillar to the top of the previous pillar
        current_top_previous_top = cable_length[pillar - 1][1] + find_wire_length(distance, heights[pillar], heights[pillar - 1])
        cable_length[pillar][1] = max(current_bottom_previous_top, current_top_previous_top)

    # Here we already know the maximum length of wire, by taking the maximum value of wire length of the last pillar
    wire_lenght= round(max(cable_length[amount_of_pillars - 1][0], cable_length[amount_of_pillars - 1][1]), 2)

    # And finally writes the result to the output file
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
