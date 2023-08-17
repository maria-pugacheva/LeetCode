import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Adjacent Indices. Time: O(n). Space: O(1)             ***
# ---------------------------------------------------------------------
# Hint: Check every three consecutive numbers in the list for parity.
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> bool:
    """Return True if there are three consecutive odd numbers in nums.

    Preconditions:
        1 <= len(nums) <= 1000
        1 <= nums[i] <= 1000

    Examples:
        >>> solution_one([5, 7])
        False
        >>> solution_one([2, 6, 4, 1])
        False
        >>> solution_one([1, 2, 34, 3, 4, 5, 7, 23, 12])
        True
    """
    for i in range(2, len(nums)):
        if nums[i] & 1 and nums[i - 1] & 1 and nums[i - 2] & 1:
            return True
    return False


# ---------------------------------------------------------------------
# Approach 2: Counter. Time: O(n). Space: O(1)                      ***
# ---------------------------------------------------------------------
# Hint: Iterate through the elements of the list.  If an element is odd,
#       increment a counter; otherwise, reset the counter to zero.
#       Whenever the counter is equal to three, return True.
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> bool:
    """Return True if there are three consecutive odd numbers in nums.

    Preconditions:
        1 <= len(nums) <= 1000
        1 <= nums[i] <= 1000

    Examples:
        >>> solution_two([5, 7])
        False
        >>> solution_two([2, 6, 4, 1])
        False
        >>> solution_two([1, 2, 34, 3, 4, 5, 7, 23, 12])
        True
    """
    cnt = 0
    for n in nums:
        if n & 1:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0
    return False


if __name__ == '__main__':
    doctest.testmod()
