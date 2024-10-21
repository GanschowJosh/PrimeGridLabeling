// TODO
// tidy-up code;
// add java docs;
// have main josh program read in coprimes from file

#include <stdio.h>
#include <stdlib.h>
#import "nodes.h"
#import "print.h"



int main() {
    int max;
    char linkedCoprimesFilePath[64] = "../../Data/linkedCoprimes.txt";
    
    FILE *outFile = fopen(linkedCoprimesFilePath, "w");
    if (outFile == NULL) {
        printf("Error opening relative file path: '%s'\n", linkedCoprimesFilePath);
        return 1;
    }

    printf("Enter max: ");
    scanf("%d", &max);

    Root* head = generateGraph(max);

    printGraph(head, outFile);

    printf("Coprime graph written to: ../Data/linkedCoprimes.txt\n");

    fclose(outFile);
}