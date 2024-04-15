"""Lab 6"""


def update_max_experience(pos, structure, stage):
    left_parent, right_parent = 0, 0
    if pos > 0:
        left_parent = structure[stage - 1][pos - 1]

    if pos < len(structure[stage - 1]):
        right_parent = structure[stage - 1][pos]

    structure[stage][pos] += max(left_parent, right_parent)


def calculate_max_experience(structure, output_file_path):

    amount_of_lines = len(structure)

    for stage in range(1, amount_of_lines):
        for pos in range(len(structure[stage])):
            update_max_experience(pos, structure, stage)

    with open(output_file_path, 'w') as file:
        file.write(str(max(structure[-1])))
