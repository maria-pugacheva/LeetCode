import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set I. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """Return a list of size 2 where:
        - answer[0] is a list of all distinct integers in nums1 which
        are not present in nums2
        - answer[1] is a list of all distinct integers in nums2 which
        are not present in nums1

    Examples:
        >>> solution_one([1, 2, 3], [2, 4, 6])
        [[1, 3], [4, 6]]
        >>> solution_one([1, 2, 3, 3], [1, 1, 2, 2])
        [[3], []]
    """
    s1 = set(nums1)
    s2 = set(nums2)
    return [list(s1 - s2), list(s2 - s1)]


# ---------------------------------------------------------------------
# Approach 2: Set II. Time: O(n) - WON'T WORK                       ***
# ---------------------------------------------------------------------
def solution_two(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """Return a list of size 2 where:
        - answer[0] is a list of all distinct integers in nums1 which
        are not present in nums2
        - answer[1] is a list of all distinct integers in nums2 which
        are not present in nums1

    Examples:
        >>> solution_two([1, 2, 3], [2, 4, 6])
        [[1, 3], [4, 6]]
        >>> solution_two([1, 2, 3, 3], [1, 1, 2, 2])
        [[3], []]
    """
    s1 = set()
    s2 = set(nums2)
    for n in nums1:
        if n in s2:
            s2.remove(n)
        else:
            s1.add(n)
    return [list(s1), list(s2)]


if __name__ == '__main__':
    doctest.testmod()
