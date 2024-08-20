import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n). Space: O(1)                 ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Remove the duplicates in-place and return the new length of nums.

    Preconditions:
        nums is sorted

    Examples:
        >>> solution([1, 2])
        2
        >>> solution([1, 1, 2, 3])
        3
        >>> solution([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        5
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    doctest.testmod()
