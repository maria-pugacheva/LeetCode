import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Bit Manipulation. Time: O(n)                          !**
# ---------------------------------------------------------------------
# Concept: The inverse of XOR is XOR.
# ---------------------------------------------------------------------
def solution(nums: List[int], f: int) -> List[int]:
    """Return an array (where array[0] == f) that was encoded into nums.

    There is a hidden integer array arr that consists of n non-negative
    integers. It was encoded into another integer array nums of length
    n - 1, such that nums[i] = arr[i] XOR arr[i + 1]. For example,
    if arr = [1, 0, 2, 1], then nums = [1, 2, 3].

    Preconditions:
        2 <= n <= 10^4
        len(nums) == n - 1
        0 <= nums[i] <= 10^5
        0 <= f <= 10^5

    Examples:
        >>> solution([1], 3)
        [3, 2]
        >>> solution([1, 2, 3], 1)
        [1, 0, 2, 1]
        >>> solution([6, 2, 7, 3], 4)
        [4, 2, 0, 7, 4]
    """
    arr = [f]
    for n in nums:
        arr.append(arr[-1] ^ n)
    return arr


if __name__ == '__main__':
    doctest.testmod()
