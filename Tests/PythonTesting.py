import time
import sys
from Scripts import GridPrimeLabeling
outputPath = f"./StressTestData {time.strftime('%Y-%m-%d %H.%M.%S')}" #output path of the file, will depend on where the script is run


#detecting file errors before stress testing
try:
    with open(outputPath, "w+") as file:
        pass
except Exception as e:
    print(e)
    sys.exit()


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
                matrix = GridPrimeLabeling.generateCoprimeMatrix(size, size)
                endTime = time.time()

                isValid, _ = GridPrimeLabeling.checkMatrix(matrix)
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
    with open(outputPath, "w+") as file:
        file.write("\nSummary:\n")
        print("\nSummary:")
        file.write("Size | Successes | Failures | Avg Time (s) | Min Time (s) | Max Time (s)\n")
        print("Size | Successes | Failures | Avg Time (s) | Min Time (s) | Max Time (s)")
        file.write(f"{'-'*70}\n")
        print("-"*70)
        for size, data in results.items():
            file.write(f"{size:4d} | {data['successes']:9d} | {data['failures']:8d} | {data['avgTime']:12.4f} | {data['minTime']:12.4f} | {data['maxTime']:12.4f}\n")
            print(f"{size:4d} | {data['successes']:9d} | {data['failures']:8d} | {data['avgTime']:12.4f} | {data['minTime']:12.4f} | {data['maxTime']:12.4f}")


if __name__ == "__main__":
    maxSize = 20 #max matrix size to test
    numTrials = 50 #number of trials for each size
    timeout = 99999 #max number of seconds to generate a single system before giving up

    results = stressTest(maxSize, numTrials, timeout)
    printSummary(results)
