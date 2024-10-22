#ifndef nodes
#define nodes

// #include <stdio.h>
// #include <stdlib.h>
// #include "maths.h"
// #include "files.h"

typedef struct Node {
    int value;
    int numberOfCoprimes;
    struct Node** coprimeArray;
    struct Node* nextNode;
} Node;

// memory fiddling + code golfing = :)
void linkCoprimes(Node* a, Node* b);

// finds every coprime for every node
void findCoprimes(Node* node, int max);

void initializeNodes(Node* node, int max);

// Generates graph of numbers that each link to their coprimes.
// Returns a pointer to the head node of the graph (holding the number 1).
Node* generateGraph(int max);

#endif