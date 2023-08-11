import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution_one(nums: List[int]) -> List[int]:
    """Return [a, b] such that a occurs twice and b is missing in nums.

    Notes:
        nums originally contained all the numbers from 1 to n.
        The numbers should be returned in the order specified above.

    Preconditions:
        2 <= len(nums) <= 10^4
        1 <= nums[i] <= 10^4

    Examples:
        >>> solution_one([1, 1])
        [1, 2]
        >>> solution_one([2, 2])
        [2, 1]
        >>> solution_one([2, 3, 1, 5, 3])
        [3, 4]
    """
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    res = [0, 0]
    for n in range(1, len(nums) + 1):
        if n not in d:
            res[1] = n
        elif d[n] > 1:
            res[0] = n
    return res


if __name__ == '__main__':
    doctest.testmod()
