import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(nums1: List[int], nums2: List[int]) -> List[int]:
    """Return an integer array res of size 2 containing common elements.

    Examples:
        >>> solution([3, 4, 2, 3], [1, 5])
        [0, 0]
        >>> solution([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6])
        [3, 4]
    """
    res = [0, 0]
    d = {}
    for n in nums1:
        d[n] = d.get(n, 0) + 1
    for n in nums2:
        if n in d:
            res[1] += 1
            if d[n] != -1:
                res[0] += d[n]
                d[n] = -1
    return res


if __name__ == '__main__':
    doctest.testmod()
