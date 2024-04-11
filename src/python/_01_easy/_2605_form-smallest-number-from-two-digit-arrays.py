import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Intersection. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(nums1: List[int], nums2: List[int]) -> int:
    """Given two arrays of unique digits nums1 and nums2, return the
    smallest number that contains at least one digit from each array.

    Examples:
        >>> solution([4, 1, 3], [5, 7])
        15
        >>> solution([5, 2, 6], [3, 1, 7])
        12
        >>> solution([3, 5, 2, 6], [3, 1, 7])
        3
    """
    i = set(nums1).intersection(nums2)
    if i:
        return min(i)
    a, b = min(nums1), min(nums2)
    return a if a == b else min(a, b) * 10 + max(a, b)


if __name__ == '__main__':
    doctest.testmod()
