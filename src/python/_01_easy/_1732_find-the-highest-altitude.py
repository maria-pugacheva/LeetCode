import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n). Space: O(1)                    ***
# ---------------------------------------------------------------------
def solution_one(gain: List[int]) -> int:
    """Given an integer array gain of length n where gain[i] is the net
    gain in altitude between points i and i + 1 for all (0 <= i < n),
    return the highest altitude of a point.

    Preconditions:
        n == gain.length
        1 <= n <= 100
        -100 <= gain[i] <= 100

    Examples:
        >>> solution_one([-5,1,5,0,-7])
        1
        >>> solution_one([-4,-3,-2,-1,4,3,2])
        0
        >>> solution_one([-5,1,5,13,3,-9,0,-7])
        17
    """
    mx = 0
    curr = 0
    for n in gain:
        curr += n
        mx = max(mx, curr)
    return mx


if __name__ == '__main__':
    doctest.testmod()
