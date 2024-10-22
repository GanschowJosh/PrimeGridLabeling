#ifndef files
#define files

#include <stdio.h>
#include "nodes.h"

FILE* openFile();

void closeFile(FILE* outFile);

void printNode(Node* node, FILE* outFile);

void printGraph(Node* node, FILE* outFile);

#endif