import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary                                                !**
# ---------------------------------------------------------------------
# Hint: Convert n to a binary number and iterate over the characters of
#       the string from right to left (because we need to start with the
#       "least significant bit"), or iterate from left to right but take
#       the length of the string into consideration.
# ---------------------------------------------------------------------
def solution(n: int) -> List[int]:
    """In the binary representation of n (0-indexed), count the number
    of even indices with value 1 and the number of odd indices with
    value 1. Return an integer array res where res = [even, odd].

    Examples:
        >>> solution(2)
        [0, 1]
        >>> solution(17)
        [2, 0]
        >>> solution(3)
        [1, 1]
    """
    b = bin(n)
    res = [0, 0]
    for i in range(2, len(b)):
        if b[i] == '1':
            if (i & 1 and len(b) & 1) or (not i & 1 and not len(b) & 1):
                res[1] += 1
            else:
                res[0] += 1
    return res


if __name__ == '__main__':
    doctest.testmod()
