import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n). Space: O(1)                 ***
# ---------------------------------------------------------------------
# Hint: Use the opposite directional two-pointer approach to obtain the
#       desired result.
# ---------------------------------------------------------------------
def solution_one(s: List[str]) -> List[str]:
    """Reverse s.

    Examples:
        >>> solution_one([])
        []
        >>> solution_one(['h', 'e', 'l', 'l', 'o'])
        ['o', 'l', 'l', 'e', 'h']
        >>> solution_one(['H', 'a', 'n', 'n', 'a', 'h'])
        ['h', 'a', 'n', 'n', 'a', 'H']
    """
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


if __name__ == '__main__':
    doctest.testmod()