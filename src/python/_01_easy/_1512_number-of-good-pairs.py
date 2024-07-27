import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n^2)                             ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Return the number of good pairs in nums. A pair (i, j) is called
    good if nums[i] == nums[j] and i < j.

    Preconditions:
        1 <= len(nums) <= 100
        1 <= nums[i] <= 100

    Examples:
        >>> solution_one([1, 2, 3])
        0
        >>> solution_one([1, 1, 1, 1])
        6
        >>> solution_one([1, 2, 3, 1, 1, 3])
        4
    """
    cnt, n = 0, len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 2: Hash Table. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int]) -> int:
    """Return the number of good pairs in nums. A pair (i, j) is called
    good if nums[i] == nums[j] and i < j.

    Preconditions:
        1 <= len(nums) <= 100
        1 <= nums[i] <= 100

    Examples:
        >>> solution_two([1, 2, 3])
        0
        >>> solution_two([1, 1, 1, 1])
        6
        >>> solution_two([1, 2, 3, 1, 1, 3])
        4
    """
    cnt, seen = 0, {}
    for n in nums:
        if n in seen:
            cnt += seen[n]
        seen[n] = seen.get(n, 0) + 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
