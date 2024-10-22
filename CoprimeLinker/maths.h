#ifndef maths
#define maths

// divides(a, b) is equivalent to the statement "a divides b".
int divides(int divisor, int dividend);

/**
 <Returns whether integers a and b are coprime.>
 
 @param a smaller natural number
 @param b larger natural number
 @return 0: a and b are not coprime.
 @return 1: a and b are coprime.
 */
int areCoprime(int a, int b);

#endif