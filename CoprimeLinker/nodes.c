#include <stdlib.h>
#include "maths.h"
#include "files.h"
#include "nodes.h"

void linkCoprimes(Node* a, Node* b) {
    // assign b as a coprime of a
    (*a).numberOfCoprimes++;
    (*a).coprimeArray = (Node**) realloc((*a).coprimeArray, (*a).numberOfCoprimes * (sizeof(Node)));
    (*a).coprimeArray[(*a).numberOfCoprimes - 1] = b;

    if (a == b) return; // keeps duplicate node from getting operated on twice

    // assign a as a coprime of b
    (*b).numberOfCoprimes++;
    (*b).coprimeArray = (Node**) realloc((*b).coprimeArray, (*b).numberOfCoprimes * (sizeof(Node)));
    (*b).coprimeArray[(*b).numberOfCoprimes - 1] = a;
}

void findCoprimes(Node* node, int max, int verbosity) {
    // prepare file to be written to
    FILE* outFile = openFile();

    // loop through every node from [1,max]
    while (node != NULL) {
        Node* candidate = node;
        // loop through every candidate from [node,max]
        while (candidate != NULL) {
            // check if node and candidate are coprimes
            if (areCoprime((*node).value, (*candidate).value)) {
                // link node and candidate as coprimes (bidirectional)
                linkCoprimes(node, candidate);
            }
            // try next candidate
            candidate = (*candidate).nextNode;
        }

        // print progress
        if (verbosity == 1) printf("Wrote coprimes for %d of %d...\n", (*node).value, max);

        // write node to file
        writeNode(node, outFile);

        // prepare next node
        Node* lastNode = node;
        node = (*node).nextNode;

        // free last node's coprime array from memory
        free((*lastNode).coprimeArray);
    }

    // close file
    closeFile(outFile, verbosity);
}

void initializeNodes(Node* node, int max, int verbosity) {
    if (verbosity == 1) printf("Initializing nodes...\n");

    Node* lastNode;
    for (int value = 1; value < max + 1; value++) {
        (*node).value = value;
        (*node).numberOfCoprimes = 0;
        lastNode = node;
        node = (Node*) malloc(sizeof(Node));
        (*lastNode).nextNode = node;
    }
    (*lastNode).nextNode = NULL;
}

Node* generateGraph(int max, int verbosity) {
    Node* head = (Node*) malloc(sizeof(Node));
    initializeNodes(head, max, verbosity);
    findCoprimes(head, max, verbosity);
    return head;
}