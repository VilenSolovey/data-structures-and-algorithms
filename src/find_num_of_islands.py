"""Lab 5"""
from collections import deque

def count_number_of_islands(input_file_path,output_file_path):
    grid = []
    with open(input_file_path, 'r') as file:
        for line in file:
            if line.strip().startswith('['):
                sub_grid = [int(num) for num in line.strip().strip('[],').split(',')]
                grid.append(sub_grid)

    num_rows, num_cols = len(grid), len(grid[0])
    amount_of_islands = 0
    visited = set()

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                bfs(row, col, grid, visited, num_rows, num_cols)
                amount_of_islands = amount_of_islands + 1

    with open(output_file_path, 'w') as file:
        file.write(str(amount_of_islands))

    return amount_of_islands
def bfs(current_row, current_col, grid, visited, num_rows, num_cols):
    queue_for_bfs = deque()
    queue_for_bfs.append((current_row, current_col))
    visited.add((current_row, current_col))

    cell_neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while queue_for_bfs:
        current_row, current_col = queue_for_bfs.popleft()

        for row_id, col_id in cell_neighbours:
            if (0 <= current_col + col_id < num_cols and
                    0 <= current_row + row_id < num_rows and
                    grid[current_row + row_id][current_col + col_id] == 1 and
                    (current_row + row_id, current_col + col_id) not in visited):
                visited.add((current_row + row_id, current_col + col_id))
                queue_for_bfs.append((current_row + row_id, current_col + col_id))
