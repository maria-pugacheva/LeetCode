import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Partial Sum. Time: O(n)                               ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Given a 0-indexed integer array nums, return a 0-indexed integer
    array res where: res[i] = |leftSum[i] - rightSum[i]|.

    Examples:
        >>> solution([1])
        [0]
        >>> solution([1, 1])
        [1, 1]
        >>> solution([10, 4, 8, 3])
        [15, 1, 11, 22]
    """
    right, left, res = sum(nums), 0, []
    for n in nums:
        right -= n
        res.append(abs(right - left))
        left += n
    return res


if __name__ == '__main__':
    doctest.testmod()
