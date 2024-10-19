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

    nums = list(reversed(sorted(range(prod(dims)), key=count_unique_factors)))
    matrix = MatrixGraph(*dims)

    def recurse(g: Graph, nums: list[int]) -> Graph | None:
        """
        Given a (empty or partially labeled) Graph object and list of numbers yet to be labeled,
        recursively attempts to generate a prime labeling, returning
        None if no answer is found
        """

        # get every unlabeled node in order of highest degree -> smallest degree
        # (It's easier to label high degree nodes early on)
        nodes = (node for node in reversed(g.nodes_by_degree()) if node.get_value() is None)

        for node in nodes:
            for num in nums:
                neighbor_values = (neighbor.get_value() for neighbor in node.get_neighbors())

                for neighbor_value in neighbor_values:
                    if neighbor_value is None:
                        continue
                    if not areCoprime(neighbor_value, num):
                        break
                else:
                    # num successfully applied to graph
                    print(f"\nSet value: {num}\n")#DEBUG
                    node.set_value(num)
                    print_2d_matrix_graph(g)#DEBUG
                    nums.remove(num)

                    # base case
                    if g.is_full():
                        return g

                    next_r = recurse(g, nums)

                    if next_r is None:
                        node.set_value(None)
                        continue
                    else:
                        return next_r

        return None

    return recurse(matrix, nums)

if __name__ == "__main__":

    n, m = 5, 1

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
