import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. T: O(log n). S: O(log n)                         ^**
# ---------------------------------------------------------------------
# Complexity Analysis: Finding the next value for a given number has a
# cost of O(log n) because we are processing each digit in the number,
# and the number of digits in a number is given by log n.
# ---------------------------------------------------------------------
def solution_one(n: int) -> bool:
    """Return True if n is a happy number, and false if not.

    Examples:
        >>> solution_one(1)
        True
        >>> solution_one(2)
        False
        >>> solution_one(19)
        True
    """
    seen = set()
    while n != 1:
        t = 0
        while n > 0:
            t += (n % 10) ** 2
            n //= 10
        if t in seen:
            return False
        seen.add(t)
        n = t
    return True


# ---------------------------------------------------------------------
# Approach 2: The Only Cycle. T: O(log n). S: O(1)                  ^**
# ---------------------------------------------------------------------
def solution_two(n: int) -> bool:
    """Return True if n is a happy number, and false if not.

    Examples:
        >>> solution_two(1)
        True
        >>> solution_two(2)
        False
        >>> solution_two(19)
        True
    """
    nums = {4, 16, 37, 58, 89, 145, 42, 20}
    while n != 1:
        t = 0
        while n > 0:
            t += (n % 10) ** 2
            n //= 10
        if t in nums:
            return False
        n = t
    return True


# ---------------------------------------------------------------------
# Approach 3: While n != 4. T: O(log n). S: O(1)                    ^**
# ---------------------------------------------------------------------
def solution_three(n: int) -> bool:
    """Return True if n is a happy number, and false if not.

    Examples:
        >>> solution_three(1)
        True
        >>> solution_three(2)
        False
        >>> solution_three(19)
        True
    """
    while n != 1 and n != 4:
        t = 0
        while n > 0:
            t += (n % 10) ** 2
            n //= 10
        n = t
    return n == 1


if __name__ == '__main__':
    doctest.testmod()
