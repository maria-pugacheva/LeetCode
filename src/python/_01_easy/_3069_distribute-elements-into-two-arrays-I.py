import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Distribute all the elements of nums between two arrays nums1 and
    nums2 using n operations.

    Examples:
        >>> solution([2, 1, 3])
        [2, 3, 1]
        >>> solution([5, 4, 3, 8])
        [5, 3, 4, 8]
    """
    nums1 = [nums[0]]
    nums2 = [nums[1]]
    for i in range(2, len(nums)):
        if nums1[-1] > nums2[-1]:
            nums1.append(nums[i])
        else:
            nums2.append(nums[i])
    return nums1 + nums2


if __name__ == '__main__':
    doctest.testmod()
