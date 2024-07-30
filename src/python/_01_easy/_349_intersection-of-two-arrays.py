import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(m log m + n log n). Space: O(m + n)     ***
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
        [2]
        >>> solution_one([1, 2, 2, 1, 2], [2, 2, 2])
        [2]
        >>> solution_one([4, 9, 5], [9, 4, 9, 8, 4])
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
            if len(res) == 0 or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
            j += 1
    return res


# ---------------------------------------------------------------------
# Approach 2: Hash Set. Time: O(m + n). Space: O(m + n)             ***
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
        [2]
        >>> solution_two([1, 2, 2, 1, 2], [2, 2, 2])
        [2]
        >>> solution_two([4, 9, 5], [9, 4, 9, 8, 4])
        [9, 4]
    """
    return list(set(nums1).intersection(set(nums2)))


# ---------------------------------------------------------------------
# Approach 3: One Set. Time: O(m + n). Space: O(m)                  ***
# ---------------------------------------------------------------------
def solution_three(nums1: List[int], nums2: List[int]) -> List[int]:
    """Return an array of the intersection of nums1 and nums2.

    Preconditions:
        1 <= len(nums1), len(nums2) <= 1000
        0 <= nums1[i], nums2[i] <= 1000

    Examples:
        >>> solution_three([0, 0], [0])
        [0]
        >>> solution_three([1, 2, 2, 1], [2, 2])
        [2]
        >>> solution_three([1, 2, 2, 1, 2], [2, 2, 2])
        [2]
        >>> solution_three([4, 9, 5], [9, 4, 9, 8, 4])
        [9, 4]
    """
    def compare(setToCompare, nums):
        res = []
        for n in nums:
            if n in setToCompare:
                res.append(n)
                setToCompare.remove(n)
        return res

    if len(nums1) < len(nums2):
        return compare(set(nums1), nums2)
    else:
        return compare(set(nums2), nums1)
    

if __name__ == '__main__':
    doctest.testmod()
