import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n), n = len(a) + len(b)        ***
# ---------------------------------------------------------------------
def solution(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """Return a 2D integer array res after merging similar items in
    a and b. The res array should be sorted in ascending order.

    Examples:
        >>> solution([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]])
        [[1, 7], [2, 4], [7, 1]]
        >>> solution([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]])
        [[1, 4], [2, 4], [3, 4]]
        >>> solution([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]])
        [[1, 6], [3, 9], [4, 5]]
    """
    d = {}
    for item in a:
        d[item[0]] = item[1]
    for item in b:
        d[item[0]] = d.get(item[0], 0) + item[1]
    return sorted([[k, v] for k, v in d.items()])


if __name__ == '__main__':
    doctest.testmod()
