// TODO
// tidy-up code;
// add java docs;
// interact with graph.py
// take max as argv

#include <stdio.h>
#include <stdlib.h>
#import "nodes.h"
#import "toFile.h"
#import "math.h"

int main() {
    int max;
    char linkedCoprimesFilePath[64] = "../Data/linkedCoprimes.txt";
    int debug = 0;
    
    // open file
    FILE *outFile = fopen(linkedCoprimesFilePath, "w");
    if (outFile == NULL) {
        printf("Error opening relative file path: '%s'\n", linkedCoprimesFilePath);
        return 1;
    }

    // input max
    if (debug == 0) {
        printf("Enter max: ");
        scanf("%d", &max);
    }
    else max = debug;

    // generate graph of integers and their coprimes
    Node* head = generateGraph(max);

    // prints graph to the outFile
    printGraph(head, outFile);

    printf("Coprime graph written to: %s\n", linkedCoprimesFilePath);

    fclose(outFile);
}