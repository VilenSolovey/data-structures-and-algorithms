"""Lab 5"""
from collections import deque
NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

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
def is_valid_move(next_row, next_col, grid, visited, num_rows, num_cols):
    return (0 <= next_col < num_cols and
            0 <= next_row < num_rows and
            grid[next_row][next_col] == 1 and
            (next_row, next_col) not in visited)
def bfs(current_row, current_col, grid, visited, num_rows, num_cols):
    queue_for_bfs = deque()
    queue_for_bfs.append((current_row, current_col))
    visited.add((current_row, current_col))

    while queue_for_bfs:
        current_row, current_col = queue_for_bfs.popleft()

        for row_id, col_id in NEIGHBORS:
            next_row, next_col = current_row + row_id, current_col + col_id
            if is_valid_move(next_row, next_col, grid, visited, num_rows, num_cols):
                visited.add((next_row, next_col))
                queue_for_bfs.append((next_row, next_col))
