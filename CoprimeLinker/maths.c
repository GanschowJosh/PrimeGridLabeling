#include "maths.h"

// divides(a, b) is equivalent to the statement "a divides b".
int divides(int divisor, int dividend) {
    if (dividend % divisor == 0) return 1;
    else return 0;
}

/**
 <Returns whether integers a and b are coprime.>
 
 @param a smaller natural number
 @param b larger natural number
 @return 0: a and b are not coprime.
 @return 1: a and b are coprime.
 */
int areCoprime(int a, int b) {
    // if any natural number other than 1 divides both a and b,
    // then a and b are not coprime.

    // no natural number greater than some natural number k can divide k,
    // so, since a <= b, the divisor cannot be greater than a.

    // thus, the divisors tested will be [2,a].

    // if these tests all fail, then a and b are coprime.
    
    for (int divisor = a; divisor > 1; divisor--)
        if (divides(divisor, a) && divides(divisor, b)) return 0;
    return 1;
}