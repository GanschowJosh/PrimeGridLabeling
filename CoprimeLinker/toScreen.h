#include <stdio.h>
#include <stdlib.h>

void printProgress(int current, int max) {
    system("clear");
    printf("%d.%d%% Linked...\n", current * 100 / max, current * 10000 / max);
}