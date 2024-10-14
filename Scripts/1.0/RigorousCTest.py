import subprocess
import time

def runCProgram(n, m, timeout):
    try:
        process = subprocess.Popen(['./coprimeMatrixGenerator'],
                                   stdin=subprocess.PIPE, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE,
                                   text=True)
        
        stdout, stderr = process.communicate(input=f"{n} {m}", timeout=timeout)
        
        if process.returncode != 0:
            return False, stderr
        
        lines = stdout.strip().split('\n')
        if len(lines) < n + 1:  # +1 for the "Successfully generated" line
            return False, "Invalid output format"
        
        matrix = [list(map(int, line.split())) for line in lines[-n:]]
        if any(len(row) != m for row in matrix):
            return False, "Invalid matrix dimensions"
        
        return True, matrix
    
    except subprocess.TimeoutExpired:
        process.kill()
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

def checkMatrixValidity(matrix):
    def gcd(a, b):
        a, b = abs(a), abs(b)  # Ensure non-negative inputs
        if b == 0:
            return a if a != 0 else 1  # GCD(0,0) is defined as 1
        while b:
            a, b = b, a % b
        return a

    def areCoprime(a, b):
        return gcd(a, b) == 1

    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            neighbors = []
            if i > 0: neighbors.append(matrix[i-1][j])
            if i < n-1: neighbors.append(matrix[i+1][j])
            if j > 0: neighbors.append(matrix[i][j-1])
            if j < m-1: neighbors.append(matrix[i][j+1])
            
            if not all(areCoprime(matrix[i][j], neighbor) for neighbor in neighbors):
                return False
    return True

def stressTest(maxSixe, numTrials, timeout):
    results = {}
    
    for size in range(2, maxSixe + 1):
        print(f"\nTesting {size}x{size} matrix:")
        times = []
        successes = 0
        failures = 0
        
        for _ in range(numTrials):
            startTime = time.time()
            success, result = runCProgram(size, size, timeout)
            endTime = time.time()
            
            if success:
                if checkMatrixValidity(result):
                    successes += 1
                    times.append(endTime - startTime)
                else:
                    failures += 1
                    print(f"  Warning: Generated an invalid {size}x{size} matrix")
            else:
                failures += 1
                print(f"  Error for {size}x{size} matrix: {result}")
            
            if endTime - startTime > timeout:
                print(f"  Timeout reached for {size}x{size} matrix")
                break
        
        if times:
            avgTime = sum(times)/len(times)
            minTime = min(times)
            maxTime = max(times)
            results[size] = {
                'avgTime': avgTime,
                'minTime': minTime,
                'maxTime': maxTime,
                'successes': successes,
                'failures': failures
            }
            print(f"  Successful generations: {successes}/{numTrials}")
            print(f"  Average time: {avgTime:.4f}s")
            print(f"  Min time: {minTime:.4f}s")
            print(f"  Max time: {maxTime:.4f}s")
        else:
            print(f"  No successful generations for {size}x{size} matrix")
    
    return results

def printSummary(results):
    print("\nSummary:")
    print("Size | Successes | Failures | Avg Time (s) | Min Time (s) | Max Time (s)")
    print("-" * 70)
    for size, data in results.items():
        print(f"{size:4d} | {data['successes']:9d} | {data['failures']:8d} | {data['avgTime']:12.4f} | {data['minTime']:12.4f} | {data['maxTime']:12.4f}")

if __name__ == "__main__":
    maxSixe = 20  # Maximum matrix size to test
    numTrials = 10  # Number of trials for each size
    timeout = 99999  # Maximum time (in seconds) allowed for each matrix generation

    results = stressTest(maxSixe, numTrials, timeout)
    printSummary(results)