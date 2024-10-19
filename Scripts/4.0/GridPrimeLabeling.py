import random
import sys
import time
from math import prod
from graph import MatrixGraph, Graph, print_2d_matrix_graph
from prime_tools import *

sys.setrecursionlimit(1000000000)

def generateCoprimeMatrix(*dims: int) -> MatrixGraph:
    """
    Given dimensions n, m, generates and returns a fully labeled MatrixGraph
    in which every node's value is coprime with the values of its neighbors.
    (i.e., returns a new MatrixGraph with a valid prime labeling)
    :return:
    """

    nums = list(reversed(sorted(range(1, prod(dims)+1), key=count_unique_factors)))
    matrix = MatrixGraph(*dims)

    def recurse(g: Graph, nums: list[int], depth=0) -> Graph | None:
        """
        Given an (empty or partially labeled) Graph object and a list of numbers yet to be labeled,
        recursively attempts to generate a prime labeling, returning None if no answer is found.
        """
        # get every unlabeled node in order of highest degree -> smallest degree
        nodes = (node for node in reversed(g.nodes_by_degree()) if node.get_value() is None)

        for node in nodes:
            for i, num in enumerate(nums):
                neighbor_values = (neighbor.get_value() for neighbor in node.get_neighbors())

                # Check if the number is coprime with all neighbors
                for neighbor_value in neighbor_values:
                    if neighbor_value is None:
                        continue
                    if not coprime(neighbor_value, num):
                        break
                else:
                    # num successfully applied to graph
                    node.set_value(num)
                    nums.pop(i)  # Remove num from the list

                    # base case: if the graph is full, return the result
                    if g.is_full():
                        return g

                    # recursive call to continue filling the graph
                    next_r = recurse(g, nums, depth + 1)

                    if next_r is None:
                        # backtrack: undo the number assignment and restore it to the pool
                        node.set_value(None)
                        nums.insert(i, num)
                        continue
                    else:
                        return next_r

        # If no valid configuration is found, return None to trigger backtracking
        return None

    return recurse(matrix, nums)


if __name__ == "__main__":

    n, m = 5, 5

    total_time = 0
    epoch = 30
    for i in range(epoch):
        print("|", end="")
    print()

    total_time = 0
    for i in range(epoch):
        NOW = time.time()
        matrix = generateCoprimeMatrix(n, m)
        total_time += time.time() - NOW
        print("|", end="")
    print()
    print(f"Modified algorithm average for {n}x{m} grid {total_time / epoch} seconds ({epoch} epochs)")

    print_2d_matrix_graph(matrix)
