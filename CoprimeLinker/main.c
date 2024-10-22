// TODO
// tidy-up code;
// add java docs;
// interact with graph.py
// 2^k cannot be coprime with odd??; other optimizations??

#include <stdio.h>
#include "nodes.h"

int main(int argc, char** argv) {
    int max;

    if (argc != 2) {
        printf("Wrong number of arguments, please enter a natural number\n");
        return 1;
    }

    sscanf(argv[1], "%d", &max);

    generateGraph(max);
}