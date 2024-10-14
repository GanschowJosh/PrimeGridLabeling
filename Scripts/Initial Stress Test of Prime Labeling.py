import GridPrimeLabeling
import time
from collections import defaultdict
d = defaultdict(list)
count = 0
for n in range(5, 40, 5):
    for _ in range(20):
        count += 1
        start = time.perf_counter()
        x = GridPrimeLabeling.generateCoprimeMatrix(n, n)
        print(f"({n}, {time.perf_counter()-start})")
        d[n*n].append(time.perf_counter()-start)
        if count % 50 == 0:
            print(f"Percent: {(count/2000)*100}")

for k, v in d.items():
    print(f"({k}, {sum(v)/len(v)})")
