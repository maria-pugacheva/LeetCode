import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Merge Intervals. Time: O(n)                           ***
# ---------------------------------------------------------------------
def solution(t: List[int], secs: int) -> int:
    """Given a non-decreasing integer array t, where t[i] denotes that
    Teemo attacks Ashe at second t[i], and an integer secs. An attack at
    second t will mean Ashe is poisoned during the inclusive time
    interval [t, t + secs - 1]. If Teemo attacks again before the poison
    effect ends, the timer for it is reset, and a new time is set.
    Return the total number of seconds that Ashe is poisoned.

    Examples:
        >>> solution([1, 4], 2)
        4
        >>> solution([1, 2], 2)
        3
        >>> solution([1, 2, 3, 4, 5, 6], 3)
        8
    """
    cnt = 0
    for i in range(len(t) - 1):
        if t[i] + secs >= t[i+1]:
            cnt += t[i+1] - t[i]
        else:
            cnt += secs
    return cnt + secs


if __name__ == '__main__':
    doctest.testmod()
