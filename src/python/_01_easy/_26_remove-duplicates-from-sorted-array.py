import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n). Space: O(1).                ***
# ---------------------------------------------------------------------
# 1. Create a slow pointer named i.
# 2. Use a fast pointer j to iterate over the given list and look for
#    distinct elements.
# 3. Once j reaches the end of the given list, return count + 1.
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """Remove the duplicates in-place and return the new length of nums.

    Preconditions:
        nums is sorted

    Examples:
        >>> solution_one([1, 2])
        2
        >>> solution_one([1, 1, 2, 3])
        3
        >>> solution_one([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        5
    """
    count = 1
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    doctest.testmod()
