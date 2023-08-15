import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: No Sorting. Time: O(n)                                **^
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the maximum product difference between two pairs in nums.

    Preconditions:
        4 <= len(nums) <= 10^4
        1 <= nums[i] <= 10^4

    Examples:
        >>> solution_one([1, 2, 8, 9])
        70
        >>> solution_one([5, 6, 2, 7, 4])
        34
        >>> solution_one([4, 2, 5, 9, 7, 4, 8])
        64
    """
    max_one = max_two = 0
    min_one = min_two = 10001
    for n in nums:
        if n > max_one or n > max_two:
            max_two = max(max_one, max_two)
            max_one = n
        if n < min_one or n < min_two:
            min_two = min(min_one, min_two)
            min_one = n
    return (max_one * max_two) - (min_one * min_two)


if __name__ == '__main__':
    doctest.testmod()
