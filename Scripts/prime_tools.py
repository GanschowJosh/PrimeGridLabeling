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


def coprime(x: int, y: int):
    """
        checks if two integers are relatively prime

        That is, if the only prime factor they share is '1'

        returns a boolean value

        Example:

        rel_prime(5, 10) -> False
        rel_primt(5, 13) -> True
    :param x:
    :param y:
    :return:
    """

    x_fact = set(prime_factors(x))
    y_fact = set(prime_factors(y))

    for i in x_fact:
        if i in y_fact and i != 1:
            return False

    return True
