#import "nodes.h"

/**
 <Returns the greatest common divisor for integers a and b.>
 
 @param a first integer
 @param b second integer
 @return the greatest common divisor for integers a and b.
 */
int gcd(int a, int b) {
    int max;

    // find if a or b is smaller
    if (a < b) max = a;
    else max = b;

    // test possible divisors
    for (int divisor = max; divisor > 1; divisor--) {
        if (a % divisor == 0 && b % divisor == 0) return divisor;
    }
    return 1;
}