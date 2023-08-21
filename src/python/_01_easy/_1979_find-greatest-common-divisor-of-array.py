import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1                                                        ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the greatest common divisor of the smallest number and
    largest number in nums.

    Preconditions:
        2 <= len(nums) <= 1000
        1 <= nums[i] <= 1000

    Examples:
        >>> solution_one([3, 3])
        3
        >>> solution_one([5, 2, 6, 9, 10])
        2
        >>> solution_one([7, 5, 6, 8, 3])
        1
        >>> solution_one([136, 64, 24, 16])
        8
    """
    mx = max(nums)
    mn = min(nums)
    if mx % mn == 0:
        return mn
    for n in range(mn // 2, 0, -1):
        if mn % n == 0 and mx % n == 0:
            return n


# ---------------------------------------------------------------------
# Approach 2: Euclidean Algorithm                                     !
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Return the greatest common divisor of the smallest number and
    largest number in nums.

    Preconditions:
        2 <= len(nums) <= 1000
        1 <= nums[i] <= 1000

    Examples:
        >>> solution_two([3, 3])
        3
        >>> solution_two([5, 2, 6, 9, 10])
        2
        >>> solution_two([7, 5, 6, 8, 3])
        1
        >>> solution_two([136, 64, 24, 16])
        8
    """
    mx = max(nums)
    mn = min(nums)
    while mn:
        mn, mx = mx % mn, mn
    return mx


if __name__ == '__main__':
    doctest.testmod()
