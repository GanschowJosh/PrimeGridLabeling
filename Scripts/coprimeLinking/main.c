// TODO
// tidy-up code;
// add java docs;
// have main josh program read in coprimes from file
// split into header files

#include <stdio.h>
#include <stdlib.h>

typedef struct Root {
    int value;
    struct Root* nextRoot;
    struct Coprime* nextCoprime;
} Root;

typedef struct Coprime {
    int value;
    struct Coprime* nextCoprime;
} Coprime;

/**
 <Returns the greatest common divisor for integers a and b.>
 
 @param a first integer
 @param b second integer
 @return the greatest common divisor for integers a and b.
 */
int gcd(int a, int b) {
    int max;

    // find if a or b is smaller
    if (a < b) max = a;
    else max = b;

    // test possible divisors
    for (int divisor = max; divisor > 1; divisor--) {
        if (a % divisor == 0 && b % divisor == 0) return divisor;
    }
    return 1;
}

void findCoprimes(Root* node, int max) {
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

void linkCoprimes(Root* head, int max) {
    Root* node = head;
    for (int i = 0; node != NULL; i++) {
        findCoprimes(node, max);
        printf("Linked %d / %d nodes...\n", i + 1, max);
        node = (*node).nextRoot;
    }
}

// Generates graph of numbers that each link to their coprimes.
// Returns a pointer to the head node of the graph (holding the number 1).
Root* generateGraph(int max) {
    Root* head = initializeNodes(max);
    linkCoprimes(head, max);
    return head;
}

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

int main() {
    int max;
    
    FILE *outFile = fopen("../Data/linkedCoprimes.txt", "w");
    if (outFile == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    printf("Enter max: ");
    scanf("%d", &max);

    Root* head = generateGraph(max);

    printGraph(head, outFile);

    printf("Coprime graph written to: ../Data/linkedCoprimes.txt\n");

    fclose(outFile);
}