import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n). Space: O(1)                    ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[int]:
    """Replace the values in nums and return it.

    Replace each value in the given list with the value of the greatest
    element to that element's right.  Replace the last element with -1.

    Preconditions:
        1 <= len(arr) <= 10^4
        1 <= arr[i] <= 10^5

    Examples:
        >>> solution_one([1])
        [-1]
        >>> solution_one([2, 1])
        [1, -1]
        >>> solution_one([17, 18, 5, 4, 6, 1])
        [18, 6, 6, 6, 1, -1]
    """
    curr = -1
    for i in range(len(nums) - 1, -1, -1):
        t = nums[i]
        nums[i] = curr
        curr = max(curr, t)
    return nums


if __name__ == '__main__':
    doctest.testmod()
