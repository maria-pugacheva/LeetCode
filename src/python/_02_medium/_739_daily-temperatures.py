import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Monotonic Decreasing Stack. Time: O(2n). Space: O(n)  ^**
# ---------------------------------------------------------------------
def solution_one(temps: List[int]) -> List[int]:
    """Given an array of integers temps representing daily temperatures,
    return an array answer where answer[i] is the number of days you
    have to wait after the i-th day to get a warmer temperature. If no
    such future day exists, set answer[i] to 0.

    Examples:
        >>> solution_one([30, 60, 90])
        [1, 1, 0]
        >>> solution_one([30, 40, 50, 60])
        [1, 1, 1, 0]
        >>> solution_one([73, 74, 75, 71, 69, 72, 76, 73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> solution_one([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
        [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
    """
    res = [0] * len(temps)
    stack = []  # pair: [index, temp]
    for i, t in enumerate(temps):
        while stack and stack[-1][-1] < t:
            indTemp, valTemp = stack.pop()
            res[indTemp] = i - indTemp
        stack.append([i, t])
    return res


# ---------------------------------------------------------------------
# Approach 2: Array. Time: O(2n). Space: O(1)                       ^**
# ---------------------------------------------------------------------
def solution_two(temps: List[int]) -> List[int]:
    """Given an array of integers temps representing daily temperatures,
    return an array answer where answer[i] is the number of days you
    have to wait after the i-th day to get a warmer temperature. If no
    such future day exists, set answer[i] to 0.

    Examples:
        >>> solution_two([30, 60, 90])
        [1, 1, 0]
        >>> solution_two([30, 40, 50, 60])
        [1, 1, 1, 0]
        >>> solution_two([73, 74, 75, 71, 69, 72, 76, 73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> solution_two([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
        [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
        >>> solution_two([34, 80, 80, 34, 34, 80, 80, 80, 80, 34])
        [1, 0, 0, 2, 1, 0, 0, 0, 0, 0]
    """
    res = [0] * len(temps)
    hottest = 0
    for currDayInd in range(len(temps) - 1, -1, -1):
        currTemp = temps[currDayInd]
        if currTemp >= hottest:  # use the condition `>=` to avoid a TLE
            hottest = currTemp
            continue
        days = 1
        while temps[currDayInd + days] <= currTemp:
            days += res[currDayInd + days]
        res[currDayInd] = days
    return res


if __name__ == '__main__':
    doctest.testmod()
