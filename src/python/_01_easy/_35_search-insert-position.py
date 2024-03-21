import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Check All. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], t: int) -> int:
    """Given a sorted array of distinct integers nums and a target
    value t, return the index if the target is found. If not, return
    the index where it would be if it were inserted in order.

    Examples:
        >>> solution_one([1, 3, 5, 6], 5)
        2
        >>> solution_one([1, 3, 5, 6], 2)
        1
        >>> solution_one([1, 3, 5, 6], 7)
        4
    """
    if t > nums[-1]:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] >= t:
            break
    return i


if __name__ == '__main__':
    doctest.testmod()
