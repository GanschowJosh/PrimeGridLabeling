def prime_factors(x: int) -> list[int]:
    """
        returns a sorted list of prime factors of x

        The list does not only hold unique factors,
        so by finding the product of every item in the returned list,
        the parameter x is reconstructed

        Additionally, the resulting list includes a single '1'

        Example:

        prime_factors(8) -> [1, 2, 2, 2]
        prime_factors(10) -> [1, 2, 5]
    :param x:
    :return:
    """

    l = [x]

    def divides(a, b):
        return b // a == b / a

    last_cycle = False
    while not last_cycle:

        last_cycle = True

        for i in range(len(l)):
            for j in range(2, l[i]):
                if divides(j, l[i]):
                    last_cycle = False
                    l.append(j)
                    l[i] //= j

    l_filtered = list(
        x for x in l if x != 1  # I don't know why, but 1's randomly end up in here
    )

    l_filtered.append(1)

    return sorted(l_filtered)


def count_unique_factors(n: int) -> int:
    """
    Returns an integer enumerating the number of unique prime factors of the given integer.
    :param n:
    :return:
    """
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n = n // i
    return count


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def coprime(a, b) -> bool:
    """
    Returns a boolean value indicating whether the two integers given are coprime

    That is, if the integers share no unique prime factors
    :param a:
    :param b:
    :return:
    """
    return gcd(a, b) == 1


def factors(n) -> set[set[int]]:
    """
    Returns a set of factors each integer 1...n
    """
    factors = {i: set() for i in range(1, n + 1)}
    for i in range(1, n+1):
        for factor in range(1, int(i ** 0.5) + 1):
            if i % factor == 0:
                factors[i].add(factor)
                if factor != i // factor:
                    factors[i].add(i // factor)
    return factors


def num_of_factors(n) -> set[set[int]]:
    """
    Returns number of factors of each integer 1...n
    """
    factorlist = factors(n)
    num_factors = {i: len(factorlist[i]) for i in range(1, n + 1)}
    return num_factors


def most_factors_first(n) -> list[list[int]]:
    """
    Returns a list of integers sorted backwards by how many factors they have.
    This function helps bias generate_prime_grid by trying to choose to get rid of the
    "worst" numbers as early as possible, similar to move ordering in chess:
    https://www.chessprogramming.org/Move_Ordering

    An example of this in a 90x90 grid: *7560*, with 64 factors, would be
    chosen first for the top left corner of the grid.
    """
    factor_counts = num_of_factors(n)
    sorted_list = sorted(factor_counts.items(), key=lambda item: item[1], reverse=True)
    return [item[0] for item in sorted_list]

