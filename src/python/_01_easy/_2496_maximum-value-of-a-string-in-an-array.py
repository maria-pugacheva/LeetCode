import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Try ... Except. Time: O(n)                            ***
# ---------------------------------------------------------------------
def solution(strs: List[str]) -> int:
    """Given an array strs of alphanumeric strings, return the maximum
    value of any string in strs. The value of an alphanumeric string
    can be defined as the numeric representation of the string in base
    10, if it comprises of digits only, or the length of the string,
    otherwise.

    Examples:
        >>> solution(['1', '01', '001', '0001'])
        1
        >>> solution(['alic3', 'bob', '3', '4', '00000'])
        5
        >>> solution(['5', 'abc4', '01'])
        5
    """
    res = 0
    for s in strs:
        try:
            res = max(res, int(s))
        except ValueError:
            res = max(res, len(s))
    return res


if __name__ == '__main__':
    doctest.testmod()
