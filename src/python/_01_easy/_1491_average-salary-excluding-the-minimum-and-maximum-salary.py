import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n). Space: O(n)                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> float:
    """Find the average salary of the employees whose salary is in nums.

    The minimum and maximum salary should be excluded from the average.

    Preconditions:
        3 <= len(salary) <= 100
        10^3 <= salary[i] <= 10^6
        salary[i] is unique
        answers within 10^(-5) of the actual value are acceptable

    Examples:
        >>> solution_one([1000, 2000, 3000])
        2000.0
        >>> solution_one([6000, 5000, 4000, 3000, 2000, 1000])
        3500.0
        >>> solution_one([8000, 9000, 2000, 3000, 6000, 1000])
        4750.0
    """
    nums.sort()
    return (sum(nums) - nums[0] - nums[-1]) / (len(nums) - 2)


# ---------------------------------------------------------------------
# Approach 2: MIN and MAX. Time: O(n). Space: O(1)                  ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> float:
    """Find the average salary of the employees whose salary is in nums.

    The minimum and maximum salary should be excluded from the average.

    Preconditions:
        3 <= len(salary) <= 100
        10^3 <= salary[i] <= 10^6
        salary[i] is unique
        answers within 10^(-5) of the actual value are acceptable

    Examples:
        >>> solution_two([1000, 2000, 3000])
        2000.0
        >>> solution_two([6000, 5000, 4000, 3000, 2000, 1000])
        3500.0
        >>> solution_two([8000, 9000, 2000, 3000, 6000, 1000])
        4750.0
    """
    mn = 1_000_001
    mx = -1
    total = 0
    for n in nums:
        mn = min(mn, n)
        mx = max(mx, n)
        total += n
    return (total - mn - mx) / (len(nums) - 2)


if __name__ == '__main__':
    doctest.testmod()
