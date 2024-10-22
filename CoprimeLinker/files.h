#ifndef files
#define files

#include <stdio.h>
#include "nodes.h"

FILE* openFile();

void closeFile(FILE* outFile, int verbosity);

void writeNode(Node* node, FILE* outFile);

void printGraph(Node* node, FILE* outFile);

#endif