import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting + Two Pointers. Time: O(n log n)              ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """As long as nums is not empty, find the minimum and maximum
    numbers in nums, calculate the average of the two numbers, and
    removed them. Return the number of distinct averages calculated
    using the described approach.

    Examples:
        >>> solution([1, 100])
        1
        >>> solution([4, 1, 4, 0, 3, 5])
        2
        >>> solution([5, 5, 5, 5, 5, 5])
        1
    """
    nums.sort()
    seen = set()
    for i in range(len(nums) // 2):
        seen.add((nums[i] + nums[len(nums) - 1 - i]) / 2)
    return len(seen)


if __name__ == '__main__':
    doctest.testmod()
