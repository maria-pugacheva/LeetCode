import doctest
from typing import List
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Hash Table. Time: O(m + n). Space: O(min(n, m))       ***
# ---------------------------------------------------------------------
def solution_one(nums1: List[int], nums2: List[int]) -> List[int]:
    """Return an array of the intersection of nums1 and nums2.

    Preconditions:
        1 <= len(nums1), len(nums2) <= 1000
        0 <= nums1[i], nums2[i] <= 1000

    Examples:
        >>> solution_one([0, 0], [0])
        [0]
        >>> solution_one([1, 2, 2, 1], [2, 2])
        [2, 2]
        >>> solution_one([4, 9, 5], [9, 4, 9, 8, 4])
        [9, 4]
    """
    def checkOtherMap(mapToCompare, nums):
        res = []
        for n in nums:
            if mapToCompare.get(n, 0) > 0:
                res.append(n)
                mapToCompare[n] -= 1
        return res

    if len(nums1) < len(nums2):
        return checkOtherMap(Counter(nums1), nums2)
    else:
        return checkOtherMap(Counter(nums2), nums1)


# ---------------------------------------------------------------------
# Approach 2: Sort. Time: O(m log m + n log n). Space: O(m + n)     ***
# ---------------------------------------------------------------------
def solution_two(nums1: List[int], nums2: List[int]) -> List[int]:
    """Return an array of the intersection of nums1 and nums2.

    Preconditions:
        1 <= len(nums1), len(nums2) <= 1000
        0 <= nums1[i], nums2[i] <= 1000

    Examples:
        >>> solution_two([0, 0], [0])
        [0]
        >>> solution_two([1, 2, 2, 1], [2, 2])
        [2, 2]
        >>> solution_two([4, 9, 5], [9, 4, 9, 8, 4])
        [4, 9]
    """
    res = []
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res


if __name__ == '__main__':
    doctest.testmod()
