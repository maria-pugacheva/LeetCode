import doctest


# ---------------------------------------------------------------------
# Approach 1: Integer Reversal. Time: O(log n). Space: O(1)           !
# ---------------------------------------------------------------------
# Hint: Try reversing the given integer.  Note that if the last digit
#       of the integer is 0, in order for the integer to be a
#       palindrome, the first digit of it also needs to be 0.  Special
#       attention should be given to the integers with an odd number of
#       digits.
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
        >>> solution_one(124)
        False
        >>> solution_one(-121)
        False
    """
    if n < 0 or (n != 0 and n % 10 == 0):
        return False
    temp = n // 10
    rev = n % 10
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return n == rev


# ---------------------------------------------------------------------
# Approach 2: String Conversion. Time: O(n)                           *
# ---------------------------------------------------------------------
# Hint: Convert the given integer to a string.  Then, use two pointers
#       to check if the given integer is a palindrome.
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
        >>> solution_one(124)
        False
        >>> solution_one(-121)
        False
    """
    if n < 0 or (n != 0 and n % 10 == 0):
        return False
    s = str(n)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    doctest.testmod()
