import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Passes. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """If nums[i] == nums[i + 1], multiply nums[i] by 2 and set
    nums[i + 1] to 0. After performing the above, shift all the 0's to
    the end of the array.

    Examples:
        >>> solution([0, 1])
        [1, 0]
        >>> solution([1, 0, 0])
        [1, 0, 0]
        >>> solution([1, 2, 2, 1, 1, 0])
        [1, 4, 2, 0, 0, 0]
    """
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i], nums[i + 1] = nums[i] * 2, 0
    j = 0
    for k in range(len(nums)):
        if nums[j] != 0:
            j += 1
        elif nums[k] != 0:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
    return nums


if __name__ == '__main__':
    doctest.testmod()
