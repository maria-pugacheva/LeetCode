import doctest


# ---------------------------------------------------------------------
# Approach 1: Bit Manipulation. Time: O(log n). Space: O(1)           !
# ---------------------------------------------------------------------
# Hint: The relationship between the given integer and its complement
#       number is the following: input + output = '111...111' in binary.
#       Example: 5 ('101') + 2 ('010') = 7 ('111' in binary).
# ---------------------------------------------------------------------
# 1. Construct a bit mask of 1's. Its decimal representation should be
#    greater or equal to the given integer.
# 2. Find the complement as follows: mask – n OR mask ^ n, where n is
#    the given integer.
#
#    Given n = 5. Construct the mask and then use XOR.
#    Left shift: 1 << 1 = 2 ('10') + 1 ('1') => 3 ('11')
#                3 << 1 = 6 ('110') + 1 ('1') => 7 ('111')
#           XOR: 5 ('101') ^ 7 ('111') = 2 ('010' -> '10')
# ---------------------------------------------------------------------
def solution_one(n: int) -> int:
    """Find the complement of the binary representation of n.

    Notes:
        The complement strategy is to flip the bits of the binary
        representation of an integer.

    Preconditions:
        0 <= n < 10^9

    Examples:
        >>> solution_one(0)
        1
        >>> solution_one(1)
        0
        >>> solution_one(5)
        2
        >>> solution_one(4523)
        3668
    """
    mask = 1
    while mask < n:
        mask = (mask << 1) + 1
    return mask ^ n


if __name__ == '__main__':
    doctest.testmod()
