import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> int:
    """An ant is on a boundary. It sometimes goes left and sometimes
    right. Return the number of times the ant returns to the boundary.

    Examples:
        >>> solution_one([2, 3, -5])
        1
        >>> solution_one([3, 2, -3, -4])
        0
        >>> solution_one([2, 3, -5, -5, 4, 1])
        2
    """
    cnt = steps = 0
    for n in nums:
        steps += n
        if steps == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
