import time
import sys

path = input("Enter the path to the folder containing your `GridPrimeLabeling.py` file: ")
version = path.split("/")[-1] #inferring version number is the last directory
#adding folder of current test file
sys.path.insert(0, path)
from GridPrimeLabeling import generateCoprimeMatrix, checkMatrix

def stressTest(maxSize, numTrials, timeout):
    results = {}

    for size in range(2, maxSize + 1):
        print(f"\nTesting {size}x{size} matrix:")
        times = []
        successes = 0
        failures = 0

        for _ in range(numTrials):
            startTime = time.time()

            try:
                matrix = generateCoprimeMatrix(size, size)
                endTime = time.time()

                isValid, _ = checkMatrix(matrix)
                if isValid:
                    successes += 1
                    times.append(endTime - startTime)
                
                else:
                    failures += 1
                    print(f" Warning: Generated an invalid {size}x{size} matrix")
                
            except RecursionError:
                failures += 1
                print(f"  Recursion error for {size}x{size} matrix")
            
            if time.time() - startTime > timeout:
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
    with open(f"../../Data/{version}/RigorousPythonData", "w") as file:
        file.write("\nSummary:\n")
        print("\nSummary:")
        file.write("Size | Successes | Failures | Avg Time (s) | Min Time (s) | Max Time (s)\n")
        print("Size | Successes | Failures | Avg Time (s) | Min Time (s) | Max Time (s)")
        file.write(f"{"-"*70}\n")
        print("-"*70)
        for size, data in results.items():
            file.write(f"{size:4d} | {data['successes']:9d} | {data['failures']:8d} | {data['avgTime']:12.4f} | {data['minTime']:12.4f} | {data['maxTime']:12.4f}\n")
            print(f"{size:4d} | {data['successes']:9d} | {data['failures']:8d} | {data['avgTime']:12.4f} | {data['minTime']:12.4f} | {data['maxTime']:12.4f}")


if __name__ == "__main__":
    maxSize = 20 #max matrix size to test
    numTrials = 25 #number of trials for each size
    timeout = 256 #max number of seconds to generate a single system before giving up

    results = stressTest(maxSize, numTrials, timeout)
    printSummary(results)
