import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_one(arr: List[str], k: int) -> str:
    """Return the kth distinct str present in arr, or an empty str.

    Notes:
        The strings are considered in the order in which they appear in
        the list.

    Preconditions:
        1 <= k <= len(arr) <= 1000
        1 <= len(arr[i]) <= 5
        arr[i] consists of lowercase English letters

    Examples:
        >>> solution_one(['a', 'b', 'a'], 3)
        ''
        >>> solution_one(['aaa', 'aa', 'a'], 1)
        'aaa'
        >>> solution_one(['d', 'b', 'c', 'b', 'c', 'a'], 2)
        'a'
    """
    d = {}
    for s in arr:
        d[s] = d.get(s, 0) + 1
    for s in arr:
        if d[s] == 1:
            k -= 1
            if k == 0:
                return s
    return ''


if __name__ == '__main__':
    doctest.testmod()
