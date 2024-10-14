import random
import sys
import math

sys.setrecursionlimit(1000000000)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def areCoprime(a, b):
    return gcd(a, b) == 1

def getNeighbors(matrix, i, j):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
            neighbors.append(matrix[ni][nj])
    return neighbors

def isValid(matrix, i, j, value):
    neighbors = getNeighbors(matrix, i, j)
    return all(areCoprime(value, neighbor) for neighbor in neighbors if neighbor != 0)

def generateCoprimeMatrix(n, m):
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
                return generateCoprimeMatrix(n, m)

    return matrix

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:3d}" for num in row))

def checkMatrix(matrix):
    n, m  = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if not isValid(matrix, i, j, matrix[i][j]):
                return False, (i, j)
    return True, None

if __name__ == "__main__":
    n, m = 20, 20
    result = generateCoprimeMatrix(n, m)
    printMatrix(result)
    print(checkMatrix(result)[0])