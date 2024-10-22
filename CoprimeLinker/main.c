// TODO
// tidy-up code;
// add java docs;
// interact with graph.py

#include <stdio.h>
//#include <stdlib.h>
#include "nodes.h"
//#include "nodes.c"
//#include "files.h"

int main(int argc, char** argv) {
    int max;

    if (argc != 2) {
        printf("Wrong number of arguments, please enter a natural number\n");
        return 1;
    }

    sscanf(argv[1], "%d", &max);

    // generate graph of integers and their coprimes
    generateGraph(max);

    // prints graph to the outFile
    // printGraph(head, outFile);
}