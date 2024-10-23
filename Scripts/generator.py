from GridPrimeLabeling import generate_prime_grid
from graph import print_2d_matrix_graph
from time import perf_counter
from os import makedirs

# Range of NxN grids to generate
START_N = 1
END_N = 20

OUTPUT_FOLDER = "grids/"  # ensure '/' at the end
FILE_FORMAT = "{i}x{i}.txt"  # what the files will be named

# Ensure the output folder exists
makedirs(OUTPUT_FOLDER, exist_ok=True)

# Meat & potatoes of the generator
total_start = perf_counter()
for i in range(START_N, END_N + 1):
    start = perf_counter()  # keep track of elapsed time
    print(f"Generating {i}x{i} grid... ", end="")

    # Perform the generation
    prime_grid = generate_prime_grid(i, i)
    delta = round(perf_counter() - start, 4)

    # If valid grid exists, save it
    if prime_grid is not None:
        print(f"Success! ({delta}s)")
        # Save successful grids in output directory
        with open(OUTPUT_FOLDER + FILE_FORMAT.format(i=i), "w") as f:
            f.write(
                print_2d_matrix_graph(prime_grid, True)
            )
    else:  # Grid generation failed
        print(f"FAILED! ({delta}s).")

total_time = round(perf_counter() - total_start, 2)
print(f"All done!! ({total_time}s)")