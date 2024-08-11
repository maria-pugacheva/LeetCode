import doctest
import math

# ---------------------------------------------------------------------
# Approach 1: Sieve of Eratosthenes. Time: O(sqrt(n)*log(log n) + n)  !
# ---------------------------------------------------------------------
# Complexity analysis. The +n is from calculating the answer after the
# main algorithm. The sqrt(n) comes from the outer loop. Each time we
# hit a prime, we "cross out" the multiples of that prime because we
# know they aren't prime. the time complexity of "crossing out" is
# log(log n). 
# ---------------------------------------------------------------------
def solution(n: int) -> int:
    """Given an integer n, return the number of prime numbers that are
    strictly less than n.

    Examples:
        >>> solution(10)
        4
        >>> solution(0)
        0
        >>> solution(1)
        0
    """
    primes, limit = [True] * n, int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    return sum(primes) - 2 if n > 2 else 0


if __name__ == '__main__':
    doctest.testmod()
