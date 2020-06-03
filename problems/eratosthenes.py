"""
    Sieve of Eratosthenes algorithm
    - Problem: Print all prime numbers equal or less than n
    - Prime(a natural number with only divisors, 1 and itself)
"""


def sieve(n):
    if not n:
        return n
    if 1 >= n:
        return n
    n += 1

    boolean_value = [True for each_number in range(n)]
    boolean_value[0] = boolean_value[1] = False
    number = 2

    while number ** 2 <= n:

        if boolean_value[number]:

            for multiple_of_num in range(number ** 2, n, number):
                boolean_value[multiple_of_num] = False

        number += 1

    return [i for i, val in enumerate(boolean_value) if val]
