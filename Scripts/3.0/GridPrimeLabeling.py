import random
import sys
import math
import time
from graph import MatrixGraph, print_2d_matrix_graph


sys.setrecursionlimit(1000000000)


def count_unique_factors(n: int) -> int:
    """
        Returns an integer enumerating the number of unique prime factors of the given integer.
    :param n:
    :return:
    """
    count=0
    for i in range(2,n):
        if n%i==0:
           count+=1
           while n%i==0:
               n=n//i
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

def generateCoprimeMatrix_old(n: int, m: int) -> list[list[int]]:
    """
        Attempts to generate and return a two-dimensional list where each element is coprime with
        all of its orthogonal neighbors. (deprecated)
    :param n:
    :param m:
    :return:
    """
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    numbers = list(range(1, n*m + 1))
    random.shuffle(numbers)

    for i in range(n):
        for j in range(m):
            for num in numbers:
                if isValid(matrix, i, j, num):
                    matrix[i][j] = num
                    numbers.remove(num)
                    break
            else:
                # If no valid number is found, start over
                return generateCoprimeMatrix_old(n, m)

    return matrix

def generateCoprimeMatrix(n, m) -> MatrixGraph:
    """
        Given dimensions n, m, generates and returns a fully labeled MatrixGraph
        in which every node's value is coprime with the values of its neighbors.
        (i.e., returns a new MatrixGraph with a valid prime labeling)
    :param n:
    :param m:
    :return:
    """
    maxFactors = 1
    for i in range(1,n*m+1):
        if count_unique_factors(i) > count_unique_factors(maxFactors):
            maxFactors = i

    def generator(n, m, maxFactors):
        """
            An interior function of generateCoprimeMatrix, used to isolate
            logic needed in the recursive step. The use of generateCoprimeMatrix as an outer function
            also hides the use of maxFactors from the outer function caller.
        :param n:
        :param m:
        :param maxFactors:
        :return:
        """
        matrix_graph = MatrixGraph(n, m)
        numbers = list(range(2,n*m+1))
        random.shuffle(numbers)
        # move number with max factors to the beginning and 1 to the end
        numbers.remove(maxFactors)
        numbers.insert(0, maxFactors)
        numbers.append(1)

        for coord in matrix_graph.possible_coords():
            for num in numbers:
                if isValid(matrix_graph, coord, num):
                    matrix_graph.get_node_by_coord(coord).set_value(num)
                    numbers.remove(num)
                    break
            else:
                # If no valid number is found, start over
                return generator(n, m, maxFactors)

        return matrix_graph

    return generator(n, m, maxFactors)


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

    total_time=0
    epoch=30
    for i in range(epoch):
        print("|",end="")
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
        total_time+=time.time()-NOW
        print("|", end="")
    print()
    print(f"Modified algorithm average for {n}x{m} grid {total_time/epoch} seconds ({epoch} epochs)")

    print_2d_matrix_graph(matrix)