import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Slicing. Time: O(n)                                   ***
# ---------------------------------------------------------------------
def solution(details: List[str]) -> int:
    """Each element of details provides information about a given
    passenger compressed into a string of length 15. Return the number
    of passengers who are strictly older than 60 years old.

    Examples:
        >>> solution(['7823570031M6122', '7813390034F6017'])
        1
        >>> solution(['7823570031M7519', '7813390034F9050'])
        2
        >>> solution(['7848571131M1523'])
        0
    """
    cnt = 0
    for p in details:
        if int(p[11:13]) > 60:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
