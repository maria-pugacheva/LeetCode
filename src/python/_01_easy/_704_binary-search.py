import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(log n)                         ***
# ---------------------------------------------------------------------
def solution(nums: List[int], t: int) -> int:
    """Return the index of t in nums, or -1 if it does not occur.

    Preconditions:
        nums is sorted (in ascending order)
        all elements in nums are unique
        1 <= len(nums) <= 10000
        -9999 <= nums[i] <= 9999

    Examples:
        >>> solution([2], 2)
        0
        >>> solution([-1, 0, 3, 5, 9, 12], 9)
        4
        >>> solution([-1, 0, 3, 5, 9, 12], 2)
        -1
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == t:
            return mid
        elif nums[mid] < t:
            i = mid + 1
        else:
            j = mid - 1
    return -1


if __name__ == '__main__':
    doctest.testmod()
