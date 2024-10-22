#include "maths.h"

// divides(a, b) is equivalent to the statement "a divides b".
int divides(int divisor, int dividend) {
    if (dividend % divisor == 0) return 1;
    else return 0;
}

/**
 <Returns whether integers a and b are coprime.>
 
 @param a first integer
 @param b second integer
 @return 0: a and b are not coprime.
 @return 1: a and b are coprime.
 */
int areCoprime(int a, int b) {
    int max;

    // find if a or b is smaller
    if (a < b) max = a;
    else max = b;

    // test possible divisors
    for (int divisor = max; divisor > 1; divisor--)
        if (divides(divisor, a) && divides(divisor, b))
            return 0;
    return 1;
}