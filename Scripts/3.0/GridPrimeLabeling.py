import random
import sys
import math
import time


def count_unique_factors(n):
    count=0
    for i in range(2,n):
        if n%i==0:
           count+=1
           while n%i==0:
               n=n//i
    return count
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
def generateCoprimeMatrix_modified(n, m,maxfactors):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    numbers = list(range(2,n*m+1))
    random.shuffle(numbers)
    # move number with max factors to the beginning and 1 to the end
    numbers.remove(maxfactors)
    numbers.insert(0, maxfactors)
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
                return generateCoprimeMatrix_modified(n, m,maxfactors)

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


    n, m = 8, 8

    total_time=0
    epoch=30
    for i in range(epoch):
        print("|",end="")
    print()

    #original algorithm
    for i in range(epoch):
        NOW = time.time()
        generateCoprimeMatrix(n, m)
        total_time+=time.time()-NOW
        print("|",end="")
    print()
    print(f"Original algorithm average for {n}x{m} grid {total_time / epoch} seconds ({epoch} epochs)")

    #weighted algorithm
    total_time=0
    max_f = 1
    for i in range(1,n*m+1):
        if count_unique_factors(i) > count_unique_factors(max_f):
            max_f = i
    for i in range(epoch):
        NOW = time.time()
        generateCoprimeMatrix_modified(n, m,max_f)
        total_time+=time.time()-NOW
        print("|", end="")
    print()
    print(f"Modified algorithm average for {n}x{m} grid {total_time/epoch} seconds ({epoch} epochs)")