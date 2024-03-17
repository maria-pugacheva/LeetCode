import doctest


# ---------------------------------------------------------------------
# Approach 1: Odd or Even. Time: O(n)                                 ^
# ---------------------------------------------------------------------
# In this game, the only move that can change the parity (evenness or
# oddness) of the number on the chalkboard is subtracting 1. Hence,
# if Alice starts with an even number, she can always subtract 1 to give
# Bob an odd number. And since all divisors of an odd number are odd,
# Bob can only give Alice an even number. This way, Alice can ensure
# that she always plays on even numbers and Bob always plays on odd
# numbers, which ensures that Bob will eventually receive a 1 and lose
# the game.
# ---------------------------------------------------------------------
def solution(n: int) -> bool:
    """Alice and Bob take turns playing a game, with Alice starting
    first. Initially, there is a number n on the chalkboard. Each player
    chooses any x (0 < x < n and n % x == 0) and replaces the number n
    on the chalkboard with n - x. Return True if and only if Alice wins
    the game, assuming both players play optimally.

    Examples:
        >>> solution(1)
        False
        >>> solution(2)
        True
        >>> solution(3)
        False
    """
    return not n & 1


if __name__ == '__main__':
    doctest.testmod()
