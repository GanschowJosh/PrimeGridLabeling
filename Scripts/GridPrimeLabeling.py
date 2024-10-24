from math import gcd
from graph import *
from prime_tools import most_factors_first


def is_valid(matrix: MatrixGraph, i, j, num) -> bool:
    """
    Returns a boolean value indicating whether a number is coprime with values of
    every filled node adjacent to the given grid coordinate
    """
    neighbors_value_raw = (neighbor.get_value() for neighbor in matrix.get_node_by_coord([i, j]).get_neighbors())
    neighbors_value = (value for value in neighbors_value_raw if value is not None)
    return all(gcd(num, neighbor_value) == 1 for neighbor_value in neighbors_value)


def generate_prime_grid(n, m) -> MatrixGraph | None:
    """
    Backtracking approach that uses most_factors_first to try to place numbers
    with more unique prime factors first when the likelihood of finding a valid position for
    that number is higher.
    """
    swap_inx = 0

    # Loop through all possible swap indices
    while swap_inx < n * m:
        grid = MatrixGraph(n, m)

        # Generate numbers sorted by most prime factors
        nums = most_factors_first(n * m)

        # Pop element with index swap_inx and insert it at the beginning
        # Basically, try a different number as the first number
        popped = nums.pop(swap_inx)
        nums.insert(0, popped)

        stack = []
        index = 0

        # Begin attempting to fill the grid
        while index < n * m:
            row, col = divmod(index, m)
            placed = False
            tried_numbers = set()

            # Try to place a valid number in the grid
            for num in nums:
                if num not in tried_numbers and is_valid(grid, row, col, num):
                    grid.get_node_by_coord([row, col]).set_value(num)
                    stack.append((index, num))
                    nums.remove(num)
                    placed = True
                    break
                tried_numbers.add(num)

            if placed:
                index += 1
            # Backtrack if we couldn't place a number
            else:
                if not stack:
                    break  # Couldn't backtrack any further
                # Undo the previous placement
                while stack:
                    prev_index, prev_num = stack.pop()
                    row, col = divmod(prev_index, m)
                    grid.get_node_by_coord([row, col]).set_value(0)
                    nums.append(prev_num)
                    tried_numbers.add(prev_num)
                    index = prev_index
                    if len(tried_numbers) < len(nums):
                        break
                else:
                    break  # If backtrack fails, stop and try a different swap_inx

        # If the grid is fully populated, return the grid
        if index == n * m:
            return grid

        # Try again with a next number as the first
        swap_inx += 1

    # Wow, we couldn't find a prime-labeled grid?
    return None # if the code reaches this, we're screwed.
