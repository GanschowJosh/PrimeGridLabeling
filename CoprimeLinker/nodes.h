#ifndef nodes
#define nodes

typedef struct Node {
    int value;
    int numberOfCoprimes;
    struct Node** coprimeArray;
    struct Node* nextNode;
} Node;

// memory fiddling + code golfing = :)
void linkCoprimes(Node* a, Node* b);

// finds every coprime for every node
void findCoprimes(Node* node, int max, int verbosity);

void initializeNodes(Node* node, int max, int verbosity);

// Generates graph of numbers that each link to their coprimes.
// Returns a pointer to the head node of the graph (holding the number 1).
Node* generateGraph(int max, int verbosity);

#endif