# Version 4.0
In this version, I introduced a backtracking algorithm. It is a stack-based approach that tries to place the 'worst' numbers early on in the grid, allowing for fast speed optimizations.

# Goal
Our team's goal is to build an efficient algorithm that generates a matrix of a prime labeled graph. Ideally, we would be able to generate a 90x90 matrix in under a minute (that's a grid with 8100 prime-labeled vertices!).

This goal has been met on 10/20, when a 113x113 was found, which took 23 seconds, meeting our goal.

# Building on an Old Approach
Version 3.0 used a randomly shuffled list with John's optimization of inserting a single, most factorable integer in the beginning. The shuffling nature of this algorithm makes its speed unpredictable and usually suboptimal.

The philosophy of version 4.0 is to use a stack that attempts to use most heavily-factored numbers first. See `v4.py`. This algorithm is deterministic since it does not use randomness, but instead, a high-factor-biased list to try to attempt to use the 'worst' numbers first, so ideally, the grid doesn't face neighboring problems with highly factorable numbers deeper into the search, cutting down on time.

# Features
As mentioned earlier, this script is **deterministic**, meaning it doesn't use randomness, and it generates the same grids each time it runs.

This script runs **much quicker than the v3 version** of the [PrimeGridLabeling project](https://github.com/GanschowJosh/PrimeGridLabeling). As an example, it created a 45x45
grid on my i7-9700 in 0.63 seconds, and a 115x115 grid in 25.44 seconds!

It's also fair to note that (in my opinion), this is fairly **simple to install** and run on your own computer, and see all the grids that the algorithm generated.

The generator.py script now features multiprocessing to take advantage of multiple cores when generating grid ranges. In my testing, this brought the generation of NxN grids 1...40 from 30 seconds to just under 9 on an eight-core CPU.

# Try this out!
## Prereqs
Download the ZIP for this repo.

Install [Python](https://www.python.org/downloads/)
- tested on 3.10.6 and 3.11.2, but any of the latest versions should work.

This script only needs NumPy to work, so install it with
> `pip install numpy`

On linux machines, pip may complain about externally managed environments;

In that case, you may need to use a [virtual environment](https://docs.python.org/3/library/venv.html).

## Okay, show me the results!!
Running `generator.py` is the easiest way to demonstrate this script in action.

Steps:
- Leave the START_N as it is
- Set END_N to be the upper bound for how big NxN array you wish to create
- 64 is a good number for the upper bound, 48 if your computer is a bit slow
- Run the script
- See your CPU's hard work in folder `grids`, which includes a `_successful-grids.txt` list of all NxN grids the script could generate, and a corresponding txt file for each grid.

# Interesting findings
A previous issue of the original implementation of my algorithm was the fact that the algorithm could only generate grids with the most-factorable number in the top-left corner. This issue has been fixed, and the algorithm has successfully generated grids of 60x60+ sizes.
> Previously, successful grids up to N=155 were `1 2 3 4 5 6 7 8 9 10 11 14 15 16 17 18 19 25 27 28 29 30 31 34 37 45 61 113 115`.
These successful grids, as can be concluded from the issue, all had solutions with the most factorable number in the top left corner!

We have yet to calculate the time complexity of the algorithm and gather data on the trendline of data size vs. time to calculate the grid.

As Github user [GanschowJosh](https://github.com/GanschowJosh) mentioned in [this repository](https://github.com/GanschowJosh/PrimeGridLabeling), this is an interesting project to take on, as the concept can be mapped to find the prime labeling of a graph.
