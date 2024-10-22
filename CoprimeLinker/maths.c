#include "maths.h"

int divides(int divisor, int dividend) {
    if (dividend % divisor == 0) return 1;
    else return 0;
}

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