import random
import sys
# import math
import time

sys.setrecursionlimit(1000000000)

def count_unique_factors(n: int) -> int:
    """
    Count the number of factors, 2...n-1, of n
    """
    count = 0
    for i in range(2, n):
        if n % i == 0:
           count += 1
           while n % i == 0:
               n = n // i
    return count

def gcd(a: int, b: int) -> int:
    """
    Uses the Euclidean algorithm to find the GCD.
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
    while b:
        a, b = b, a % b
    return a

def areCoprime(a: int, b: int) -> bool:
    """
    Return true if a and b are coprime
    a and b are coprime if their greatest common denominator is 1

    """
    return gcd(a, b) == 1

def getNeighbors(matrix: list[list[int]], i: int, j: int) -> list[int]:
    """
    Check the orthogonal (non-diagonal) neighbors of matrix(i, j)
    Returns the values of the neighbors.
    """
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
            neighbors.append(matrix[ni][nj])
    return neighbors

def isValid(matrix: list[list[int]], i: int, j: int, value: int) -> bool:
    """
    Check true/false if the current matrix is valid.
    """
    neighbors = getNeighbors(matrix, i, j)
    return all(areCoprime(value, neighbor) for neighbor in neighbors if neighbor != 0)

def generateCoprimeMatrix_old(n: int, m: int) -> list[list[int]]:
    """
    Generates a Coprime n*m Matrix by brute-force.
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

def generateCoprimeMatrix(n: int, m: int):
    """
    Slightly optimized implementation of generateCoprimeMatrix_old()
    Recursive solution to make implementation of the stress testing utility script easier
    """
    maxFactors = 1
    for i in range(1, n * m + 1):
        if count_unique_factors(i) > count_unique_factors(maxFactors):
            maxFactors = i

    def generator(n: int, m: int, maxFactors: int) -> list[list[int]]:
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        numbers = list(range(2,n*m+1))
        random.shuffle(numbers)
        # move number with max factors to the beginning and 1 to the end
        numbers.remove(maxFactors)
        numbers.insert(0, maxFactors)
        numbers.append(1)

        for i in range(n):
            for j in range(m):
                for num in numbers:
                    if isValid(matrix, i, j, num):
                        matrix[i][j] = num
                        numbers.remove(num)
                        break
                else:
                    # If no valid number is found, start over
                    return generator(n, m, maxFactors)

        return matrix

    return generator(n, m, maxFactors)

def printMatrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(" ".join(f"{num:3d}" for num in row))

def checkMatrix(matrix: list[list[int]]) -> tuple[bool, tuple[int]]:  # todo change return type to a single tuple
    n, m  = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if not isValid(matrix, i, j, matrix[i][j]):
                return False, (i, j)
    return True, None

if __name__ == "__main__":
    n, m = 8, 8

    total_time = 0
    epoch = 30
    for i in range(epoch):
        print("|", end="")
    print()

    # original algorithm
    for i in range(epoch):
        NOW = time.time()
        generateCoprimeMatrix_old(n, m)
        total_time += time.time() - NOW
        print("|",end="")
    print()
    print(f"Original algorithm average for {n}x{m} grid {total_time / epoch} seconds ({epoch} epochs)")

    total_time = 0
    for i in range(epoch):
        NOW = time.time()
        generateCoprimeMatrix(n, m)
        total_time += time.time() - NOW
        print("|", end="")
    print()
    print(f"Modified algorithm average for {n}x{m} grid {total_time/epoch} seconds ({epoch} epochs)")