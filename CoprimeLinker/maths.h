#ifndef maths
#define maths

/**
 * Checks if the divisor can divide the dividend and returns if they divide.
 * divides(a, b) is equivalent to the statement "a divides b".
 * 
 * @param divisor Attempts to divide the dividend.
 * @param dividend Attempts to be divided by the divisor.
 * @return int 1 if divides, 0 if not divides.
 */
int divides(int divisor, int dividend);

/**
 * Takes two natural numbers and returns if they are coprime.
 * 
 * @param a Smaller natural number.
 * @param b Larger natural number.
 * @return int 1 if coprime, 0 if not coprime.
 */
int areCoprime(int a, int b);

#endif