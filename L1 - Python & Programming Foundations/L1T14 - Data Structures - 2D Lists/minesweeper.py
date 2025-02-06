def generate_minesweeper_grid(grid):
    # Define the dimensions of the grid

    rows, cols = len(grid), len(grid[0])

    # Function to count the mines around a given cell
    def count_adjacent_mines(r, c):
        # List of possible adjacent positions
        positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for pos in positions:
            new_r, new_c = r + pos[0], c + pos[1]
            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '#':
                count += 1
        return count

    # Create a new grid to store the counts
    new_grid = [['' for _ in range(cols)] for _ in range(rows)]

    # Calculate the number of adjacent mines for each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                new_grid[r][c] = '#'
            else:
                new_grid[r][c] = str(count_adjacent_mines(r, c))

    return new_grid

# Example usage
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

output_grid = generate_minesweeper_grid(input_grid)
for row in output_grid:
    print(row)
