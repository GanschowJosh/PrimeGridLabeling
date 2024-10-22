#ifndef nodes
#define nodes

/**
 * Contains a value, number of associated coprimes (including self),
 * dynamic list of pointers to coprime nodes, and the pointer to the next node.
 */
typedef struct Node {
    int value;
    int numberOfCoprimes;
    struct Node** coprimeArray;
    struct Node* nextNode;
} Node;

/**
 * Adds node a to node b's index of its coprimes and vice versa.
 * 
 * @param a Pointer to a node.
 * @param b Pointer to a node.
 */
void linkCoprimes(Node* a, Node* b);

/**
 * Finds and links the coprimes for every node.
 * 
 * @param node A pointer to the head node of the graph (1).
 * @param max The largest number in the graph.
 * @param verbosity Specifies if status updates are printed to the terminal.
 */
void findCoprimes(Node* node, int max, int verbosity);

/**
 * Creates a linked list of nodes from [1,max].
 * Coprimes are not yet linked.
 * 
 * @param node A pointer to the head node of the graph (1).
 * @param max The largest number in the graph.
 * @param verbosity Specifies if status updates are printed to the terminal.
 */
void initializeNodes(Node* node, int max, int verbosity);

/**
 * Creates a graph of nodes from [1,max] with coprimes interlinked.
 * 
 * @param max The largest number in the graph.
 * @param verbosity Specifies if status updates are printed to the terminal.
 * @return Node* A pointer to the head node of the graph (1).
 */
Node* generateGraph(int max, int verbosity);

#endif