#import "nodes.h"

void printNode(Node* node, FILE* outFile) {
    // prints the value of node
    fprintf(outFile, "%d:", (*node).value);

    // prints each of node's coprimes
    for (int i = 0; i < (*node).numberOfCoprimes; i++) {
        if ((*node).coprimeArray[i] == (*node).coprimeArray[i + 1]) continue; // prevents from printing twice
        fprintf(outFile, " %d", (*(*node).coprimeArray[i]).value);
    }

    // newline
    fprintf(outFile, "\n");
}

void printGraph(Node* node, FILE* outFile) {
    while (node != NULL) {
        printNode(node, outFile);
        node = (*node).nextNode;
    }
}