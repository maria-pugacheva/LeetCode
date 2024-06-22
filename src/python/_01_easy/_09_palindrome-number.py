import doctest


# ---------------------------------------------------------------------
# Approach 1: Integer Reversal. Time: O(log n). Space: O(1)           !
# ---------------------------------------------------------------------
def solution_one(n: int) -> bool:
    """Determine whether n is a palindrome.

    Examples:
        >>> solution_one(7)
        True
        >>> solution_one(10)
        False
        >>> solution_one(121)
        True
        >>> solution_one(2332)
        True
        >>> solution_one(124)
        False
        >>> solution_one(-121)
        False
    """
    if n < 0 or (n != 0 and n % 10 == 0):
        return False
    rev = 0
    while n > rev:
        rev = rev * 10 + n % 10
        n //= 10
    return n == rev or n == rev // 10


# ---------------------------------------------------------------------
# Approach 2: String Conversion. Time: O(n)                         ***
# ---------------------------------------------------------------------
def solution_two(n: int) -> bool:
    """Determine whether n is a palindrome.

    Examples:
        >>> solution_one(7)
        True
        >>> solution_one(10)
        False
        >>> solution_one(121)
        True
        >>> solution_two(2332)
        True
        >>> solution_one(124)
        False
        >>> solution_one(-121)
        False
    """
    if n < 0 or (n != 0 and n % 10 == 0):
        return False
    n = str(n)
    i, j = 0, len(n) - 1
    while i < j:
        if n[i] != n[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    doctest.testmod()
