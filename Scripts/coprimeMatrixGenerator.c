#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// Maximum size for the matrix
#define MAX_SIZE 100

// How many grids are in each generation
#define population 100

// Probability of a random mutation (swap of numbers in the grid)
#define mutation_rate 0.03
#define crossover_rate 0.5

int num_rows, num_cols;

int gcf(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Scoring function (lower score is better)
// Each point of score means an adjacent pair shares a factor
int score(int arr[], int rows, int cols) {
    int sum = 0;
    for (int r = 0; r < rows - 1; r++) {
        for (int c = 0; c < cols - 1; c++) {
            int right = (gcf(arr[cols * r + c], arr[r * cols + c + 1]));
            if (right > 1) {
                sum += 1;
            }
            int down = (gcf(arr[cols * r + c], arr[(1 + r) * cols + c]));
            if (down > 1) {
                sum += 1;
            }
        }
    }
    for (int i = 0; i < rows - 1; i++) {
        int top = (cols - 1) + i * cols;
        int bottom = (cols - 1) + (i + 1) * cols;
        int sc = gcf(arr[top], arr[bottom]);
        if (sc > 1) {
            sum += 1;
        }
    }
    for (int i = 0; i < cols - 1; i++) {
        int left = (rows - 1) * cols + i;
        int right = (rows - 1) * cols + i + 1;
        int sc = gcf(arr[left], arr[right]);
        if (sc > 1) {
            sum += 1;
        }
    }
    return sum;
}

void print_arr(int arr[], int rows, int cols) {
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            printf("%d ", arr[cols * r + c]);
        }
        printf("\n");
    }
}

void shuffle(int *array, size_t n) {
    if (n > 1) {
        size_t i;
        for (i = 0; i < n - 1; i++) {
            size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
            int t = array[j];
            array[j] = array[i];
            array[i] = t;
        }
    }
}

void initialize(int* arr) {
    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            arr[num_cols * i + j] = num_cols * i + j + 1;
        }
    }
}

void cross(int* A, int* B) {
    int size = num_rows * num_cols;
    bool nums[MAX_SIZE * MAX_SIZE + 1] = {false};
    int* C = malloc(size * sizeof(int));

    int split = rand() % (size);

    for (int i = 0; i < split; i++) {
        C[i] = A[i];
        nums[C[i]] = true;
    }
    int index = split;
    int B_index = 0;
    while (index < size) {
        if (nums[B[B_index]] == false) {
            nums[B[B_index]] = true;
            C[index] = B[B_index];
            index += 1;
        }
        B_index += 1;
    }
    for (int i = 0; i < size; i++) {
        B[i] = C[i];
    }
    free(C);
}

void create_population(int* arr[]) {
    int size = num_rows * num_cols;
    for (int i = 0; i < population; i++) {
        arr[i] = malloc(size * sizeof(int));
        initialize(arr[i]);
        shuffle(arr[i], size);
    }
}

int* play(int* arr[]) {
    int* scores = malloc(population * sizeof(int));
    for (int i = 0; i < population; i++) {
        scores[i] = score(arr[i], num_rows, num_cols);
    }
    return scores;
}

void mutate(int* genome) {
    int size = num_rows * num_cols;
    int a = rand() % size;
    int b = rand() % size;
    int temp = genome[a];
    genome[a] = genome[b];
    genome[b] = temp;
}

int* train(int* arr[population]) {
    int size = num_rows * num_cols;
    int* scores = play(arr);

    double sum = 0;
    for (int i = 0; i < population; i++) {
        sum += scores[i];
    }
    double average = sum / population;
    for (int i = 0; i < population; i++) {
        for (int j = 0; j < population; j++) {
            if (scores[i] == 0) {
                print_arr(arr[i], num_rows, num_cols);
                return arr[i];
            }
            if (scores[i] < average && scores[j] > average && (rand() % 100) / 100.0 < crossover_rate) {
                cross(arr[i], arr[j]);
            }
        }
    }

    for (int i = 0; i < population; i++) {
        if ((rand() % 100) / 100.0 < mutation_rate) {
            mutate(arr[i]);
        }
    }

    return NULL;
}

int main() {
    srand(time(NULL));

    // Read input dimensions
    if (scanf("%d %d", &num_rows, &num_cols) != 2 || num_rows <= 0 || num_cols <= 0 || num_rows > MAX_SIZE || num_cols > MAX_SIZE) {
        fprintf(stderr, "Invalid input. Please enter two positive integers not exceeding %d.\n", MAX_SIZE);
        return 1;
    }

    int* arr[population];
    create_population(arr);
    int* done = train(arr);
    while (done == NULL) {
        done = train(arr);
    }

    printf("Successfully generated coprime matrix:\n");
    print_arr(done, num_rows, num_cols);

    // Free allocated memory
    for (int i = 0; i < population; i++) {
        free(arr[i]);
    }

    return 0;
}