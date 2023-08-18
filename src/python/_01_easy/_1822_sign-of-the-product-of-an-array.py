import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(n)                                      ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the sign of the product of all values in nums.

    Preconditions:
        1 <= len(nums) <= 1000
        -100 <= nums[i] <= 100

    Examples:
        >>> solution_one([1, 5, 0, 2, -3])
        0
        >>> solution_one([-1, 1, -1, 1, -1])
        -1
        >>> solution_one([-1, -2, -3, -4, 3, 2, 1])
        1
    """
    cnt = 0
    for n in nums:
        if n < 0:
            cnt += 1
        elif n == 0:
            return 0
    return -1 if cnt & 1 else 1


if __name__ == '__main__':
    doctest.testmod()
