#include <stdlib.h>
#include "files.h"

// relative file path for linked coprime output
char linkedCoprimesFilePath[64] = "../Data/linkedCoprimes.txt";

FILE* openFile() {
    FILE *outFile = fopen(linkedCoprimesFilePath, "w");
    if (outFile == NULL) {
        printf("Error opening relative file path: '%s'\n", linkedCoprimesFilePath);
        exit(1);
    }
    return outFile;
}

void closeFile(FILE* outFile, int verbosity) {
    if (verbosity == 1) printf("Coprime graph saved as: %s\n", linkedCoprimesFilePath);
    fclose(outFile);
}

void writeNode(Node* node, FILE* outFile) {
    // prints the value of node
    fprintf(outFile, "%d:", (*node).value);

    // prints coprimes of node
    for (int i = 0; i < (*node).numberOfCoprimes; i++) {
        if ((*node).coprimeArray[i] == (*node).coprimeArray[i + 1]) continue; // prevents from printing twice
        fprintf(outFile, " %d", (*(*node).coprimeArray[i]).value);
    }

    // newline
    fprintf(outFile, "\n");
}