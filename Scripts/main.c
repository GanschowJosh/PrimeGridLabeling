// TODO
// tidy-up code;
// add java docs;
// re-impliment Node.coprimes as linked list for dynamic allocation;
// have output go to file rather than std out
// have main josh program read in coprimes from file
// split into head files

#include <stdio.h>
#include <stdlib.h>

#define COPRIME_ARRAY_LENGTH 8100

typedef struct Node {
    int value;
    int numberOfCoprimes;
    struct Node* next;
    struct Node* coprimes[COPRIME_ARRAY_LENGTH];
} Node;

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

// Finds the node that contains value n.
Node* findNode(Node* head, int n) {
    Node* node = head;
    while(/*node != NULL*/ 1) {
        if ((*node).value == n) return node;
        else node = (*node).next;
    }
    // return NULL;
}

void findCoprimes(Node* head, Node* node, int max) {
    // 1 is always coprime
    (*node).coprimes[0] = head;

    // loop through each potential coprime from 2 to max (inclusive)
    for (int coprimeCandidate = 2; coprimeCandidate < max + 1; coprimeCandidate++) {
        // node and candidate are coprime if their gcd is 1
        if (gcd((*node).value, coprimeCandidate) == 1) {
            // add candidate to list of coprimes of node
            (*node).coprimes[(*node).numberOfCoprimes] = findNode(head, coprimeCandidate);
            (*node).numberOfCoprimes++;
        }
    }
}

Node* initializeNodes(int max) {
    printf("Initializing nodes...\n");

    // initialize head node which contains the number 1
    Node* head = (Node*) malloc(sizeof(Node));
    (*head).value = 1;
    (*head).numberOfCoprimes = 1;
    (*head).next = NULL;
    for (int j = 0; j < COPRIME_ARRAY_LENGTH; j++) {
        (*head).coprimes[j] = NULL;
    }

    // initialize body nodes
    Node* nodeOld = head;
    for (int i = 2; i < max + 1; i++) {
        Node* node = (Node*) malloc(sizeof(Node));
        (*node).value = i;
        (*node).numberOfCoprimes = 1;
        
        for (int j = 0; j < COPRIME_ARRAY_LENGTH; j++) {
            (*node).coprimes[j] = NULL;
        }

        (*nodeOld).next = node;
        nodeOld = node;
    }
    (*nodeOld).next = NULL;

    return head;
}

void linkCoprimes(Node* head, int max) {
    Node* node = head;
    for (int i = 0; i < max; i++) {
        findCoprimes(head, node, max);
        printf("Linked %d / %d nodes...\n", i + 1, max);
        node = (*node).next;
    }
}

// Generates graph of numbers that each link to their coprimes.
// Returns a pointer to the head node of the graph (holding the number 1).
Node* generateGraph(int max) {
    Node* head = initializeNodes(max);
    linkCoprimes(head, max);
    return head;
}

void printNode(Node* node, char* verbosity) {
    printf("%d\n", (*node).value);
    if (*verbosity == 'v') {
        for (int i = 0; i < (*node).numberOfCoprimes; i++) {
            if (i == (*node).numberOfCoprimes - 1)
                printf("└── %d\n", (*(*node).coprimes[i]).value);
            else
                printf("├── %d\n", (*(*node).coprimes[i]).value);
        }
    }
}

void printGraph(Node* node, char* verbosity) {
    while (node != NULL) {
        printNode(node, verbosity);
        node = (*node).next;
    }
}

int main() {
    int max;
    char verbosity;

    printf("Enter max: ");
    scanf("%d", &max);

    printf("Print nodes (p), print nodes with coprimes (v), no output (n): ");
    scanf(" %c", &verbosity);

    Node* head = generateGraph(max);

    if (verbosity == 'p' || verbosity == 'v')
        printGraph(head, &verbosity);
}
