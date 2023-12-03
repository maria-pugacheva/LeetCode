import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the maximum amount of water a container can store.

       Preconditions:
           n == len(nums)
           2 <= n <= 10^5
           0 <= nums[i] <= 10^4

       Examples:
           >>> solution_one([1, 1])
           1
           >>> solution_one([1, 8, 6, 2, 5, 4, 8, 3, 7])
           49
       """
    res = i = 0
    j = len(nums) - 1
    while i < j:
        res = max(res, (j - i) * min(nums[i], nums[j]))
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
    return res


if __name__ == '__main__':
    doctest.testmod()
