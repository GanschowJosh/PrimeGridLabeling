#import "nodes.h"

void printNode(Root* node, FILE* outFile) {
    fprintf(outFile, "%d:", (*node).value);
    Coprime* coprime = (*node).nextCoprime;
    while (coprime != NULL) {
        fprintf(outFile, " %d", (*coprime).value);
        coprime = (*coprime).nextCoprime;
    }
    fprintf(outFile, "\n");
}

void printGraph(Root* node, FILE* outFile) {
    while (node != NULL) {
        printNode(node, outFile);
        node = (*node).nextRoot;
    }
}