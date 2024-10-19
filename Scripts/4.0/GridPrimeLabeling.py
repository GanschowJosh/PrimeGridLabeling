import random
import sys
import time
from math import prod
from graph import MatrixGraph, Graph, print_2d_matrix_graph

sys.setrecursionlimit(1000000000)


def count_unique_factors(n: int) -> int:
    """
    Returns an integer enumerating the number of unique prime factors of the given integer.
    :param n:
    :return:
    """
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n = n // i
    return count


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def areCoprime(a, b) -> bool:
    """
    Returns a boolean value indicating whether the two integers given are coprime

    That is, if the integers share no unique prime factors
    :param a:
    :param b:
    :return:
    """
    return gcd(a, b) == 1


def isValid(matrix: MatrixGraph, coord: list[int], value: int) -> bool:
    """
    Takes a MatrixGraph object, the coordinate of a node, and an integer value

    Returns a boolean indicating if that value is coprime with the values of all the neighbors of
    the node at the given coordinate.

    :param matrix:
    :param coord:
    :param value:
    :return:
    """
    neighbor_values = (node.get_value() for node in matrix.get_node_by_coord(coord).get_neighbors())
    return all(areCoprime(value, neighbor_value) for neighbor_value in neighbor_values if neighbor_value is not None)


def generateCoprimeMatrix(*dims: int) -> MatrixGraph:
    """
    Given dimensions n, m, generates and returns a fully labeled MatrixGraph
    in which every node's value is coprime with the values of its neighbors.
    (i.e., returns a new MatrixGraph with a valid prime labeling)
    :return:
    """

    list(reversed(sorted(range(prod(dims)), key=count_unique_factors)))
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
                    if not areCoprime(neighbor_value, num):
                        break
                else:
                    # num successfully applied to graph
                    node.set_value(num)
                    nums.remove(num)

                    # base case
                    if g.is_full():
                        return g

        return None








def checkMatrix(matrix: MatrixGraph) -> bool:
    """
    For every node in a MatrixGraph, check that it's value is coprime with the values of it's neighbors

    Returns a boolean value
    :param matrix:
    :return:
    """

    for coord in matrix.possible_coords():

        # This could be done way cleaner, but not using isValid.
        # I want to rewrite this script to not use the current isValid, but not yet - Burke
        if not isValid(matrix, coord, matrix.get_node_by_coord(coord).get_value()):
            return False, tuple(coord)

    return True, None


def printMatrix(matrix: list[list[int]]):
    """
    Format and print a two-dimensional list of ints to stdout
    :param matrix:
    :return:
    """
    for row in matrix:
        print(" ".join(f"{num:3d}" for num in row))


if __name__ == "__main__":

    n, m = 8, 8

    total_time = 0
    epoch = 30
    for i in range(epoch):
        print("|", end="")
    print()

    # refactoring isValid to use MatrixGraph objects broke the old algorithm. If you want that
    # ported to the graph library too I'll do that - Burke
    # #original algorithm
    # for i in range(epoch):
    #     NOW = time.time()
    #     generateCoprimeMatrix_old(n, m)
    #     total_time+=time.time()-NOW
    #     print("|",end="")
    # print()
    # print(f"Original algorithm average for {n}x{m} grid {total_time / epoch} seconds ({epoch} epochs)")

    total_time = 0
    for i in range(epoch):
        NOW = time.time()
        matrix = generateCoprimeMatrix(n, m)
        total_time += time.time() - NOW
        print("|", end="")
    print()
    print(f"Modified algorithm average for {n}x{m} grid {total_time / epoch} seconds ({epoch} epochs)")

    print_2d_matrix_graph(matrix)
