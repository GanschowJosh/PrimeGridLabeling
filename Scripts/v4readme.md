# prime-grid-labeling
Generate an NxM 2d matrix such that all orthogonal neighbors are coprime.

\*this is a testing version of the [PrimeGridLabeling project](https://github.com/GanschowJosh/PrimeGridLabeling)

# Goal
Our team's goal is to build an efficient algorithm that generates a matrix of a prime labeled graph. Ideally, we would be able to generate a 90x90 matrix in under a minute (that's a grid with 8100 prime-labeled vertices!).

As of 10/20, ~5:30pm, I've found a 113x113 solution, which I have yet to validate. It took about 23 seconds. If this works, my target efficiency has been met.

Read [this paper](https://www.rroij.com/open-access/some-prime-labeling-of-graph.pdf) to learn more about prime labeling.

# Building on an Old Approach
The goal right now is to use a stack that attempts to use most heavily-factored numbers first. See v4.py. Tested for 10x10 grid.
This algorithm is deterministic since it does not use randomness, but instead, a high-factor-biased list to try to attempt to use the 'worst' numbers first.

Overall, my intuition is that selecting the "worst", or most heavily factored numbers first, should help by making the later re-arrangements easier, since
the worst numbers have been already taken care of earlier in the grid. I'm very confident in this approach, and am testing my 113x113 solution for validity.

# Features
As mentioned earlier, this script is **deterministic**, meaning it doesn't use randomness, and it generates the same grids each time it runs.

This script runs **much quicker than the v3 version** of the [PrimeGridLabeling project](https://github.com/GanschowJosh/PrimeGridLabeling). As an example, it created a 45x45
grid on my i7-9700 in 0.63 seconds, and a 115x115 grid in 25.44 seconds!

It's also good to note that (in my opinion), this is fairly **simple to install** and run on your own computer, and see all the grids that the algorithm generated.

# Try this out!
## Prereqs
Download the ZIP for this repo, of course.

Install [Python](https://www.python.org/downloads/) (tested version: 3.10.6)

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
Although I am not yet certain if there is simply an impossible prime labeling of a 20x20 grid or my algorithm simply does not catch it, it has been able to find numerous grids, including two grids larger than a 90x90 (namely, 113x113 and 115x115).

As the NxN dimensions increase, less and less often is a valid labeling found. This may be due to the previous finding, or a possibility that larger grids have too many numbers to prime-label correctly.

As Github user [GanschowJosh](https://github.com/GanschowJosh) mentioned in [this repository](https://github.com/GanschowJosh/PrimeGridLabeling), this is an interesting project to take on, as the concept can be mapped to find the prime labeling of a graph.

Current valid N for which NxN graphs have been found, searching up to N=155:
1 2 3 4 5 6 7 8 9 10 11 14 15 16 17 18 19 25 27 28 29 30 31 34 37 45 61 113 115

# Current issue
Some grids fail to generate despite a valid configuration. This can be demonstrated by attempting to generate a 10x20 grid, which fails, while a 20x10 grid returns a valid grid.

Nevertheless, the generation of 113x113 and 115x155 grids has made the efficiency tradeoff worth the accuracy sacrifice, for now.