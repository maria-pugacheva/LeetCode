import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Check Adjacent. Time: O(n)                            ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[str]:
    """Given a sorted unique integer array nums, return the smallest
    sorted list of ranges that cover all the numbers in nums exactly
    once.

    Examples:
        >>> solution_one([0])
        ['0']
        >>> solution_one([0, 1, 2, 4, 5, 7])
        ['0->2', '4->5', '7']
        >>> solution_one([0, 2, 3, 4, 6, 8, 9])
        ['0', '2->4', '6', '8->9']
    """
    ranges, start = [], 0
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i+1] - nums[i] > 1:
            r = str(nums[start])
            if start != i:
                r += '->' + str(nums[i])
            ranges.append(r)
            start = i + 1
    return ranges


if __name__ == '__main__':
    doctest.testmod()
