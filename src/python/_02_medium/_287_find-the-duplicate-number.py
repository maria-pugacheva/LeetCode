import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Floyd's Algorithm. Time: O(n)                           !
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """Given an array of integers nums containing n + 1 integers, where
    each integer is in the range [1, n], there is exactly one repeated
    number. Return the repeated number without modifying the array and
    using only constant extra space.

    Examples:
        >>> solution([1, 3, 4, 2, 2])
        2
        >>> solution([3, 1, 3, 4, 2])
        3
        >>> solution([3, 3, 3, 3, 3])
        3
    """
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


if __name__ == '__main__':
    doctest.testmod()
