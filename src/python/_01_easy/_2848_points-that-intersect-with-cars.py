import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(n log n)                             ^**
# ---------------------------------------------------------------------
def solution_one(nums: List[List[int]]) -> int:
    """Given a 0-indexed 2D integer array nums representing the
    coordinates of the cars parked on a number line, return the number
    of integer points that intersect in nums.

    Examples:
        >>> solution_one([[1, 3], [5, 8]])
        7
        >>> solution_one([[3, 6], [1, 5], [4, 7]])
        7
        >>> solution_one([[2, 3], [3, 9], [5, 7], [4, 10], [9, 10]])
        9
    """
    res = curr = 0
    nums.sort()
    for car in nums:
        if car[0] > curr:
            res += car[1] - car[0] + 1
        elif car[1] > curr:
            res += car[1] - curr
        curr = max(curr, car[1])
    return res


# ---------------------------------------------------------------------
# Approach 2: Set. Time: O(n * m)                                   ***
# ---------------------------------------------------------------------
def solution_two(nums: List[List[int]]) -> int:
    """Given a 0-indexed 2D integer array nums representing the
    coordinates of the cars parked on a number line, return the number
    of integer points that intersect in nums.

    Examples:
        >>> solution_two([[1, 3], [5, 8]])
        7
        >>> solution_two([[3, 6], [1, 5], [4, 7]])
        7
        >>> solution_two([[2, 3], [3, 9], [5, 7], [4, 10], [9, 10]])
        9
    """
    points = set()
    for car in nums:
        for i in range(car[0], car[1] + 1):
            points.add(i)
    return len(points)


if __name__ == '__main__':
    doctest.testmod()
