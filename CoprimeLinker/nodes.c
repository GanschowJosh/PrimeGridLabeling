// #include <stdio.h>
#include <stdlib.h>
//#include "maths.c"
#include "maths.h"
//#include "files.c"
#include "files.h"
#include "nodes.h"

// memory fiddling + code golfing = :)
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

// finds every coprime for every node
void findCoprimes(Node* node, int max) {
    FILE* outFile = openFile();

    printf("Finding coprimes...\n");

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
        // printf("%d / %d nodes linked...\n", (*node).value, max);
        printf("Wrote coprimes for %d of %d...\n", (*node).value, max);

        // write to file
        printNode(node, outFile);

        // try next node
        Node* lastNode = node;
        node = (*node).nextNode;

        // free last node's coprime array from memory
        free((*lastNode).coprimeArray);
    }

    closeFile(outFile);
}

void initializeNodes(Node* node, int max) {
    printf("Initializing nodes...\n");

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

// Generates graph of numbers that each link to their coprimes.
// Returns a pointer to the head node of the graph (holding the number 1).
Node* generateGraph(int max) {
    Node* head = (Node*) malloc(sizeof(Node));
    initializeNodes(head, max);
    findCoprimes(head, max);
    return head;
}