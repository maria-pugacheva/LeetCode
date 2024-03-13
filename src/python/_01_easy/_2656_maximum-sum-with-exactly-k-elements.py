import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Max. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(nums: List[int], k: int) -> int:
    """Return the maximum score you can achieve after performing the
    following operation exactly k times:

        1. Select an element m from nums
        2. Remove the selected element m from the array
        3. Add a new element with a value of m + 1 to the array
        4. Increase your score by m

    Examples:
        >>> solution([5, 5, 5], 2)
        11
        >>> solution([1, 2, 3, 4, 5], 3)
        18
    """
    n = max(nums)
    return (k * (n + n + k - 1)) // 2


if __name__ == '__main__':
    doctest.testmod()
