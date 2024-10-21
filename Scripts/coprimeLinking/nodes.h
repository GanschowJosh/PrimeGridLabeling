#include <stdio.h>
#include <stdlib.h>
#import "math.h"

typedef struct Root {
    int value;
    struct Root* nextRoot;
    struct Coprime* nextCoprime;
} Root;

typedef struct Coprime {
    int value;
    struct Coprime* nextCoprime;
} Coprime;

Root* initializeNodes(int max) {
    printf("Initializing nodes...\n");

    // initialize head node which contains the number 1
    Root* head = (Root*) malloc(sizeof(Root));
    (*head).value = 1;
    (*head).nextRoot = NULL;
    (*head).nextCoprime = NULL;

    // initialize body nodes
    Root* nodeOld = head;
    Root* node;
    for (int i = 2; i < max + 1; i++) {
        node = (Root*) malloc(sizeof(Root));
        (*node).value = i;       
        (*nodeOld).nextRoot = node;
        nodeOld = node;
    }
    (*nodeOld).nextCoprime = NULL;
    (*nodeOld).nextRoot = NULL;

    return head;
}

void linkCoprimes(Root* node, int max) {
    Coprime* coprime;
    Coprime* oldCoprime;

    // 1 is always a coprime
    coprime = (Coprime*) malloc(sizeof(Coprime));
    (*coprime).value = 1;
    (*node).nextCoprime = coprime;

    // loop through each potential coprime from 2 to max (inclusive)
    for (int coprimeCandidate = 2; coprimeCandidate < max + 1; coprimeCandidate++) {
        if (gcd((*node).value, coprimeCandidate) == 1) {
            oldCoprime = coprime;
            coprime = (Coprime*) malloc(sizeof(Coprime));
            (*coprime).value = coprimeCandidate;
            (*oldCoprime).nextCoprime = coprime;
        }
    }
    (*coprime).nextCoprime = NULL;
}

// Generates graph of numbers that each link to their coprimes.
// Returns a pointer to the head node of the graph (holding the number 1).
Root* generateGraph(int max) {
    Root* head = initializeNodes(max);
    Root* node = head;
    for (int i = 0; node != NULL; i++) {
        linkCoprimes(node, max);
        printf("Linked %d / %d nodes...\n", i + 1, max);
        node = (*node).nextRoot;
    }
    return head;
}