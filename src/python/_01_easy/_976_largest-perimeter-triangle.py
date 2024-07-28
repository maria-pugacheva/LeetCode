import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(n log n)                                ***
# ---------------------------------------------------------------------
# Hint: In a triangle, the length of any side is less than the sum of
#       the other two sides.
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Return the largest perimeter of a triangle with a non-zero area
    that can be formed from any three integers in nums.  If it is
    impossible to form any triangle of a non-zero area, return 0

    Preconditions:
        3 <= len(nums) <= 10^4
        1 <= nums[i] <= 10^6

    Examples:
        >>> solution([1, 2, 1])
        0
        >>> solution([2, 1, 2])
        5
        >>> solution([2, 1, 2, 4])
        5
        >>> solution([2, 1, 2, 3])
        7
        >>> solution([3, 2, 3, 4])
        10
        >>> solution([1, 2, 1, 10])
        0
    """
    nums.sort()
    for i in range(len(nums) - 1, 1, -1):
        if nums[i] < nums[i - 1] + nums[i - 2]:
            return nums[i] + nums[i - 1] + nums[i - 2]
    return 0


if __name__ == '__main__':
    doctest.testmod()
