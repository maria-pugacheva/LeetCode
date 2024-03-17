import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """A concatenation value of two numbers is the number formed by
    concatenating their numerals. For example, the concatenation value
    of 15 and 49 is 1549. The concatenation value of nums is initially
    equal to 0. If there exists more than one number in nums, pick the
    first element and last element in nums respectively, and add the
    value of their concatenation to the concatenation value of nums,
    then delete the first and last element from nums. Perform this step
    until nums becomes empty. Return the concatenation value.

    Examples:
        >>> solution([7])
        7
        >>> solution([7, 52, 2, 4])
        596
        >>> solution([5, 14, 13, 8, 12])
        673
    """
    res = i = 0
    j = len(nums) - 1
    while i < j:
        res = res + int(str(nums[i]) + str(nums[j]))
        i += 1
        j -= 1
    if len(nums) & 1:
        res += nums[i]
    return res


if __name__ == '__main__':
    doctest.testmod()
