import doctest
from typing import List
from collections import Counter


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(n)                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], target: List[int]) -> bool:
    """Return True if target can be formed from the elements of nums.

    Preconditions:
        len(nums) == len(target)
        1 <= len(target) <= 1000
        1 <= nums[i] <= 1000
        1 <= target[i] <= 1000

    Examples:
        >>> solution_one([7], [7])
        True
        >>> solution_one([1, 12, 1], [12, 1, 1])
        True
        >>> solution_one([3, 7, 9, 5], [3, 7, 11, 6])
        False
    """
    return sorted(nums) == sorted(target)


# ---------------------------------------------------------------------
# Approach 2: Frequency Counter. Time: O(n). Space: O(n)            ***
# ---------------------------------------------------------------------
# Hint: Each element of the target list should have a corresponding
#       element in the nums list.
# ---------------------------------------------------------------------
def solution_two(nums: List[int], target: List[int]) -> bool:
    """Return True if target can be formed from the elements of nums.

    Preconditions:
        len(nums) == len(target)
        1 <= len(target) <= 1000
        1 <= nums[i] <= 1000
        1 <= target[i] <= 1000

    Examples:
        >>> solution_two([7], [7])
        True
        >>> solution_two([1, 12, 1], [12, 1, 1])
        True
        >>> solution_two([3, 7, 9, 5], [3, 7, 11, 6])
        False
    """
    numsFreq = Counter(nums)
    for n in target:
        if n in numsFreq:
            numsFreq[n] -= 1
        if n not in numsFreq or numsFreq[n] < 0:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
