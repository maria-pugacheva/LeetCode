import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: In-Place. Time: O(n). Space: O(1)                     ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[int]:
    """Return a running sum of nums.

    Notes:
        The running sum of the input list is defined as follows:
        runningSum[i] = sum(nums[0]…nums[i]).

    Preconditions:
        1 <= len(nums) <= 1000
        -10^6 <= nums[i] <= 10^6

    Examples:
        >>> solution_one([1, 2, 3, 4])
        [1, 3, 6, 10]
        >>> solution_one([1, 1, 1, 1, 1])
        [1, 2, 3, 4, 5]
        >>> solution_one([3, 1, 2, 10, 1])
        [3, 4, 6, 16, 17]
    """
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums


# ---------------------------------------------------------------------
# Approach 2: New List. Time: O(n). Space: O(n)                     ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> List[int]:
    """Return a running sum of nums.

    Notes:
        The running sum of the input list is defined as follows:
        runningSum[i] = sum(nums[0]…nums[i]).

    Preconditions:
        1 <= len(nums) <= 1000
        -10^6 <= nums[i] <= 10^6

    Examples:
        >>> solution_two([1, 2, 3, 4])
        [1, 3, 6, 10]
        >>> solution_two([1, 1, 1, 1, 1])
        [1, 2, 3, 4, 5]
        >>> solution_two([3, 1, 2, 10, 1])
        [3, 4, 6, 16, 17]
    """
    lst = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        lst[i] = lst[i - 1] + nums[i]
    return lst


if __name__ == '__main__':
    doctest.testmod()
