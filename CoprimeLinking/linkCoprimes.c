// TODO
// tidy-up code;
// add java docs;
// interact with graph.py

#include <stdio.h>
#include <stdlib.h>
#import "nodes.h"
#import "print.h"
#import "math.h"

int main() {
    int max;
    char linkedCoprimesFilePath[64] = "../Data/linkedCoprimes.txt";
    
    // open file
    FILE *outFile = fopen(linkedCoprimesFilePath, "w");
    if (outFile == NULL) {
        printf("Error opening relative file path: '%s'\n", linkedCoprimesFilePath);
        return 1;
    }

    // input max
    printf("Enter max: ");
    scanf("%d", &max);

    // generate graph of integers and their coprimes
    Root* head = generateGraph(max);

    // prints graph to the outFile
    printGraph(head, outFile);

    printf("Coprime graph written to: %s\n", linkedCoprimesFilePath);

    fclose(outFile);
}