__author__ = 'rosoroki'

"""
Prints the sum of first n prime numbers

version 1.0

"""

import sys

def print_n_primes(_n):
    """
    Iterates through all numbers and searches for prime numbers

    Example:

    >>> print_n_primes(3)
    9
    >>> print_n_primes(100)
    24132

    """
    try:
        n = int(_n)
        if n == 1:
            return 1
        else:
            sum = 1
            current_number = 3
            primes = 1
            while primes < n:
                if is_prime(current_number):
                    sum += current_number
                    primes += 1
                current_number += 1
            return sum
    except:
        return "Something went wrong"

def is_prime(number):
    """
    Checks whether the number is prime

    Example:

    >>> is_prime(13)
    True
    >>> is_prime(100)
    False
    """

    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Please, enter first argument as 'n'")
    else:
        try:
            n = int(sys.argv[1])
            if n > 0:
                print print_n_primes(n)
            else:
                print "ENTER MORE THAN 0, STUPID ASSHOLE!!!"
        except:
            print "I'm so sorry... try again... :'("
