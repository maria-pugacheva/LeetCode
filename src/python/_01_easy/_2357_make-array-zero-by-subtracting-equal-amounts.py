import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       !**
# ---------------------------------------------------------------------
# Hint: Elements with the same value will always take the same number
#       of operations to become 0. But elements with different values
#       will always take a different number of operations to become 0.
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> int:
    """In one operation, choose a positive integer x such that x is less
    than or equal to the smallest non-zero element in nums and subtract
    x from every positive element in nums. Return the minimum number of
    operations to make every element in nums equal to 0.

    Examples:
        >>> solution([0])
        0
        >>> solution([1, 2, 1])
        2
        >>> solution([1, 5, 0, 3, 5])
        3
    """
    seen = set()
    for n in nums:
        if n != 0 and n not in seen:
            seen.add(n)
    return len(seen)


if __name__ == '__main__':
    doctest.testmod()
