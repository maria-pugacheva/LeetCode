import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n + m)                          ***
# ---------------------------------------------------------------------
def solution(nums1: List[int], nums2: List[int]) -> int:
    """Given two integer arrays nums1 and nums2, sorted in
    non-decreasing order, return the minimum integer common to both
    arrays.

    Examples:
        >>> solution([1, 2, 3], [2, 4])
        2
        >>> solution([1, 2, 3, 6], [2, 3, 4, 5])
        2
    """
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1


if __name__ == '__main__':
    doctest.testmod()
