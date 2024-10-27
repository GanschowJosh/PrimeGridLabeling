from GridPrimeLabeling import generate_prime_grid
from graph import print_2d_matrix_graph
from multiprocessing import Pool
from time import perf_counter
from os import makedirs

# Range of NxN grids to generate
START_N = 1
END_N = 40

OUTPUT_FOLDER = "grids/"  # ensure '/' at the end
FILE_FORMAT = "{i}x{i}.txt"  # what the files will be named

# Ensure the output folder exists
makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_grid(i: int) -> str:
    start = perf_counter()  # keep track of elapsed time

    # Perform the generation
    prime_grid = generate_prime_grid(i, i)
    delta = round(perf_counter() - start, 4)

    # If valid grid exists, save it
    if prime_grid is not None:
        print(f"Success! ({i}x{i} grid took {delta}s)")
        # Save successful grids in output directory
        with open(OUTPUT_FOLDER + FILE_FORMAT.format(i=i), "w") as f:
            f.write(print_2d_matrix_graph(prime_grid, True))
        return f"Success! {i}x{i} grid in {delta}s"
    else:  # Grid generation failed
        return f"FAILED!  {i}x{i} grid ({delta}s)"


if __name__ == "__main__":
    total_start = perf_counter()
    with Pool() as pool:
        results = pool.map(generate_grid, range(START_N, END_N + 1))
    
    total_time = round(perf_counter() - total_start, 2)
    print(f"All done!! ({total_time}s)")
