#ifndef files
#define files

#include <stdio.h>
#include "nodes.h"

/**
 * Opens a file in 'write' mode and returns its pointer.
 * 
 * @return FILE* Points to the created file.
 */
FILE* openFile();

/**
 * Safely closes the file at the pointer passed into it.
 * 
 * @param outFile Points to the file to be closed.
 * @param verbosity Specifies if status updates are printed to the terminal.
 */
void closeFile(FILE* outFile, int verbosity);

/**
 * Writes a given node and its coprimes to the given file.
 * 
 * @param node Contains a value and an index of other coprimes nodes.
 * @param outFile Points to the file that this node will be written to.
 */
void writeNode(Node* node, FILE* outFile);

#endif