# Prime Grid Labeling

Description: generate an n by m matrix numbered 1 to n*m where each item in the matrix is only neighbored by numbers that are coprime to the item. This can be easily mapped to the problem of finding a prime labeling of a graph in graph theory.

[Learn more](https://www.rroij.com/open-access/some-prime-labeling-of-graph.pdf) in this paper about prime labeling of graphs.

## What's new
**Version 4.0** is the most recent version of the Prime Grid Labeling project, introducing further speed optimizations with an efficient backtracking algorithm, as described [here](./Scripts/v4readme.md).

## Repo Structure

- `Scripts` folder includes all the code used.
grid = generate_prime_grid(20, 20)
print_2d_matrix_graph(grid)
    - In version `1.0` the python program is a greedy algorithm that recursively shuffles a list of numbers 1 to (n*m) and tries to place them in a locally optimal way. If there are no available numbers in the list, it calls the function again and reshuffles.
    - In version `2.0` the python program is the same, but it tries shuffling the remaining available numbers before it calls the function and wipes the slate. Additionally, uses an `lru_cache` decorator for the `gcd` and `areCoprime` functions to (hopefully) speed it up.
    - In version `3.0` user [John McMahon](https://github.com/John-A-McMahon) adds an optimization technique that places the number with the most unique factors (e.g. 6 has unique factors (1, 2, 3, and 6)) in the top left of the matrix. This is a more ideal placement of a number with many factors as the corners have the fewest neighbors.
        - Additionally, as a major step in version `3.0`, user [Burke Johnson](https://github.com/synth-mania) writes a `graph.py` module that simplifies the graph logic needed for the algorithm and rewrites the current `GridPrimeLabeling.py` to interface with said module.
    - **Version `4.0`** introduces [Iurii Chmykhun](https://github.com/blurryiurii)'s backtracking algorithm, using a stack that is ordered "worst" numbers first, that is, numbers with the most factors. The speed benefits of this algorithm allowed a 115x115 grid to be generated *in under 60 seconds*.
    - The C program (from version `1.0`) uses a genetic algorithm run for many generations with mutations built in to foster genetic diversity for the generation of systems.
    - The `Utils` folder contains the scripts made to stress test the different versions of the script. This data gets put into a file in a directory that corresponds to the provided when the script is run.

## Usage
Note on the usage of the testing file: when running the testing file, navigating to the parent directory (the main `Prime Labeling of a Grid`) and running `python -m Tests.PythonTesting` in the command line is the recommended usage. This allows the relative file paths to work properly and the `-m` flag for Python runs the specified library module as a script. The program will output the test data file to the parent folder.

The `generator.py` script can be ran from the `Scripts` directory as shown [here](./Scripts/v4readme.md#try-this-out)

## Acknowledgments
### Contributors:
1. [John McMahon](https://github.com/John-A-McMahon)
2. [Burke Johnson](https://github.com/synth-mania)
3. [Iurii Chmykhun](https://github.com/blurryiurii)
4. [Miles Roberts](https://github.com/RobertsMiles)
