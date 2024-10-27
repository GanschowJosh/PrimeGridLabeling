from math import gcd

FILENAME = "grids/20x20.txt"


def get_neighbors(i: int, j: int, rows: int, cols: int) -> list[int]:
    """
    Return the orthogonal neighbors of (i, j)
    """
    neighbors = []
    if i > 0:  # Up
        neighbors.append((i - 1, j))
    if i < rows - 1:  # Down
        neighbors.append((i + 1, j))
    if j > 0:  # Left
        neighbors.append((i, j - 1))
    if j < cols - 1:  # Right
        neighbors.append((i, j + 1))
    return neighbors


def is_valid(grid: list[list[int]], i: int, j: int, num: int, m: int, n: int) -> bool:
    """Check if num is coprime with all its orthogonal neighbors."""
    neighbors = get_neighbors(i, j, m, n)
    return all(gcd(num, grid[ni][nj]) == 1 for ni, nj in neighbors if grid[ni][nj] != 0)


def validate_prime_labeled_grid(filename: str) -> bool:
    """
    Validate that all orthogonal neighbors in the grid are coprime.
    Print where verification failed, if applicable.
    Return True if valid, False if invalid
    """
    grid = [list(map(int, line.split())) for line in open(filename, 'r').readlines()]

    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if not is_valid(grid, i, j, grid[i][j], m, n):
                print(f"Failed at ({i}, {j}) with value {grid[i][j]}")
                return False
    print("Looks good.")
    return True


validate_prime_labeled_grid(FILENAME)
