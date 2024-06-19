import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n * min(k,n))                    ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int], k: int) -> bool:
    """Find 2 numbers in nums that are equal and are at most k apart
    from each other.

    Examples:
        >>> solution_one([1, 2, 3, 1], 3)
        True
        >>> solution_one([1, 0, 1, 1], 1)
        True
        >>> solution_one([1, 2, 3, 1, 2, 3], 2)
        False
    """
    for i in range(len(nums)):
        for j in range(i+1, i+k+1):
            if j < len(nums) and nums[i] == nums[j]:
                return True
    return False


# ---------------------------------------------------------------------
# Approach 2: Hash Table. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_two(nums: List[int], k: int) -> bool:
    """Find 2 numbers in nums that are equal and are at most k apart
    from each other.

    Examples:
        >>> solution_two([1, 2, 3, 1], 3)
        True
        >>> solution_two([1, 0, 1, 1], 1)
        True
        >>> solution_two([1, 2, 3, 1, 2, 3], 2)
        False
    """
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        d[nums[i]] = i
    return False


# ---------------------------------------------------------------------
# Approach 3: Hash Set. Time: O(n)                                    !
# ---------------------------------------------------------------------
# Hint: Store only k elements in a set at all times.
# ---------------------------------------------------------------------
def solution_three(nums: List[int], k: int) -> bool:
    """Find 2 numbers in nums that are equal and are at most k apart
    from each other.

    Examples:
        >>> solution_three([1, 2, 3, 1], 3)
        True
        >>> solution_three([1, 0, 1, 1], 1)
        True
        >>> solution_three([1, 2, 3, 1, 2, 3], 2)
        False
    """
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        if len(seen) == k:
            seen.remove(nums[i-k])
        seen.add(nums[i])
    return False


if __name__ == '__main__':
    doctest.testmod()
