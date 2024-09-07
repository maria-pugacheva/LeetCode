import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. T: O(n + log n) -> O(n). S: O(n)        !!
# ---------------------------------------------------------------------
def solution_one(pairs: List[List[int]], newPair: List[int]) -> \
        List[List[int]]:
    """Given a sorted array of non-overlapping intervals pairs and a new
    interval newPair, insert the new interval into the array while
    maintaining sorted order and merging any overlapping intervals.
    Return the updated array of intervals. Note that you can make a new
    array and return it.

    Examples:
        >>> solution_one([[1, 5]], [0, 3])
        [[0, 5]]
        >>> solution_one([[1, 5]], [0, 0])
        [[0, 0], [1, 5]]
        >>> solution_one([[1, 3], [6, 9]], [2, 5])
        [[1, 5], [6, 9]]
        >>> solution_one([[1, 2], [3, 5], [8, 10], [12, 16]], [4, 8])
        [[1, 2], [3, 10], [12, 16]]
    """
    if not pairs:
        return [newPair]

    left, right = 0, len(pairs) - 1
    while left <= right:
        mid = (left + right) // 2
        if pairs[mid][0] < newPair[0]:
            left += 1
        else:
            right -= 1
    pairs.insert(left, newPair)

    res = [pairs[0]]
    for i in range(1, len(pairs)):
        if pairs[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], pairs[i][1])
        else:
            res.append(pairs[i])

    return res


# ---------------------------------------------------------------------
# Approach 2: Linear. T: O(n). S: O(1)                                !
# ---------------------------------------------------------------------
def solution_two(pairs: List[List[int]], newPair: List[int]) -> \
        List[List[int]]:
    """Given a sorted array of non-overlapping intervals pairs and a new
    interval newPair, insert the new interval into the array while
    maintaining sorted order and merging any overlapping intervals.
    Return the updated array of intervals. Note that you can make a new
    array and return it.

    Examples:
        >>> solution_two([[1, 5]], [0, 3])
        [[0, 5]]
        >>> solution_two([[1, 5]], [0, 0])
        [[0, 0], [1, 5]]
        >>> solution_two([[1, 3], [6, 9]], [2, 5])
        [[1, 5], [6, 9]]
        >>> solution_two([[1, 2], [3, 5], [8, 10], [12, 16]], [4, 8])
        [[1, 2], [3, 10], [12, 16]]
    """
    res = []

    for i in range(len(pairs)):
        if newPair[1] < pairs[i][0]:
            res.append(newPair)
            return res + pairs[i:]
        elif newPair[0] > pairs[i][1]:
            res.append(pairs[i])
        else:
            newPair[0] = min(newPair[0], pairs[i][0])
            newPair[1] = max(newPair[1], pairs[i][1])

    res.append(newPair)
    return res


if __name__ == '__main__':
    doctest.testmod()
