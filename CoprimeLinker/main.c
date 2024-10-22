// TODO
// tidy-up code;
// add java docs;
// interact with graph.py
// take max as argv; delete debug mode in main
// remove pointer to coprime array and just print coprime when is found


#include <stdio.h>
//#include <stdlib.h>
#include "nodes.h"
//#include "nodes.c"
//#include "files.h"

int main() {
    int max;
    int debug = 0;

    // input max
    if (debug == 0) {
        printf("Enter max: ");
        scanf("%d", &max);
    }
    else max = debug;

    // generate graph of integers and their coprimes
    generateGraph(max);

    // prints graph to the outFile
    // printGraph(head, outFile);
}