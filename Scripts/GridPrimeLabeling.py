from math import gcd
from graph import *
from prime_tools import most_factors_first
from sys import setrecursionlimit

setrecursionlimit(20000000)


def is_valid(matrix: MatrixGraph, i, j, num) -> bool:
    """
    Returns a boolean value indicating whether a number is coprime with values of
    every filled node adjacent to the given grid coordinate
    """
    neighbors_value_raw = (neighbor.get_value() for neighbor in matrix.get_node_by_coord([i, j]).get_neighbors())
    neighbors_value = (value for value in neighbors_value_raw if value is not None)
    return all(gcd(num, neighbor_value) == 1 for neighbor_value in neighbors_value)


# Might need to init MatrixGraph so that all nodes are zero
def generate_prime_grid(n, m, swap_inx = 0) -> MatrixGraph | None:
    """
    Backtracking approach that uses most_factors_first to try to place numbers
    with more unique prime factors first when the likelihood of finding a valid position for
    that number is higher
    """
    grid = MatrixGraph(n, m)

    nums = most_factors_first(n * m)

    # Pop element with index swap_inx and insert it into the beginning
    popped = nums.pop(swap_inx)
    nums.insert(0, popped)
    stack = []
    index = 0

    while index < n * m:
        # divmod returns the division result, then the remainder
        row, col = divmod(index, m)
        placed = False
        tried_numbers = set()

        # Try to place any number in the remaining stack
        # If a valid number is found, place it and append to stack
        # Otherwise, we didn't find a valid number and `placed = False`
        # Therefore we must backtrack
        for num in nums:
            if num not in tried_numbers and is_valid(grid, row, col, num):
                grid.get_node_by_coord([row, col]).set_value(num)
                stack.append((index, num))
                nums.remove(num)
                placed = True
                break
            tried_numbers.add(num)

        # If we got a valid number placed, we're good to go.
        # Otherwise, if we can't backtrack any further, there's no valid configuration
        # But if we can backtrack, 
        if placed:
            index += 1
        else:
            if not stack:
                return None
            # Backtrack starting from here
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
                # todo remove the need for recursion
                return generate_prime_grid(n, m, swap_inx+1)
    # Our grid is either None or completely filled
    return grid if index == n * m else None
