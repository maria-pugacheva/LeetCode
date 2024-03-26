import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(nums: List[int], key: int) -> int:
    """Return the number that appears the most after key in nums. Note:
    only one number fits this criterion.

    Examples:
        >>> solution([2, 2, 2, 2, 3], 2)
        2
        >>> solution([1, 100, 200, 1, 100], 1)
        100
        >>> solution([1, 100, 1, 100, 1, 200, 2, 1, 200, 1, 200], 1)
        200
    """
    res = mx = 0
    d = {}
    for i in range(len(nums) - 1):
        if nums[i] == key:
            k = nums[i + 1]
            d[k] = d.get(k, 0) + 1
            if d[k] > mx:
                mx = d[k]
                res = k
    return res


if __name__ == '__main__':
    doctest.testmod()
