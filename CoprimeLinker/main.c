// TODO
// tidy-up code;
// add java docs;
// interact with graph.py
// 2^k cannot be coprime with odd??; other optimizations??

#include <stdio.h>
#include "nodes.h"

int main(int argc, char** argv) {
    int max;
    int verbosity;


    if (argc != 3) {
        printf("Wrong number of arguments, please enter a natural number followed by a 1 or 0 to indicate verbosity; eg. './a.out 99 1'\n");
        return 1;
    }

    sscanf(argv[1], "%d", &max);
    sscanf(argv[2], "%d", &verbosity);

    generateGraph(max, verbosity);
}