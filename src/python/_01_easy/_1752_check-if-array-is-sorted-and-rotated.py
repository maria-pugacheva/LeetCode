import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  !**
# ---------------------------------------------------------------------
# Hint: Compare all adjacent elements (a,b) in A, the case of a > b can
#       happen at most once. The first element and the last element are
#       also connected.
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> bool:
    """Return true if nums was originally sorted in non-decreasing
    order, then rotated some number of positions (including zero).
    Otherwise, return false.

    Preconditions:
        1 <= len(nums) <= 100
        1 <= nums[i] <= 100

    Examples:
        >>> solution([1, 1, 1])
        True
        >>> solution([1, 2, 1])
        True
        >>> solution([2, 1, 3, 4])
        False
        >>> solution([3, 4, 5, 1, 2])
        True
        >>> solution([3, 4, 5, 3, 2, 3])
        False
    """
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            cnt += 1
            if cnt > 1 or nums[-1] > nums[0]:
                return False
    return True


if __name__ == '__main__':
    doctest.testmod()
