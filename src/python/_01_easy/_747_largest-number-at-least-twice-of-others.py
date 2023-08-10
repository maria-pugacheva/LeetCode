import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Tracking First and Second Max. Time: O(n)             ^**
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the index of the largest integer if it is at least twice
    as much as all other integers in nums.  Return -1 otherwise.

    Preconditions:
        1 <= len(nums) <= 50
        0 <= nums[i] <= 100
        the largest element in nums is unique

    Examples:
        >>> solution_one([1])
        0
        >>> solution_one([3, 6, 1, 0])
        1
        >>> solution_one([1, 2, 3, 4])
        -1
    """
    max_one = max_two = ind = 0
    for i in range(len(nums)):
        n = nums[i]
        if n > max_one:
            max_one, max_two = n, max_one
            ind = i
        elif n > max_two:
            max_two = n
    return ind if max_one >= max_two * 2 else -1


if __name__ == '__main__':
    doctest.testmod()
