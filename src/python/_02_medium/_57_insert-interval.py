import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Binary Search. Time: O(n). Space: O(n)                 !!
# ---------------------------------------------------------------------
def solution(pairs: List[List[int]], newPair: List[int]) -> \
        List[List[int]]:
    """You are given an array of non-overlapping intervals pairs
    where pairs[i] = [start-i, end-i] represent the start and the
    end of the i-th interval, and pairs is sorted in ascending order
    by start-i. You are also given an interval newPair = [start, end]
    that represents the start and end of another interval. Insert
    newPair into pairs such that pairs is still sorted in
    ascending order by start-i and pairs still does not have any
    overlapping intervals (merge overlapping intervals if necessary).

    Examples:
        >>> solution([[1, 5]], [0, 0])
        [[0, 0], [1, 5]]
        >>> solution([[1, 5]], [0, 3])
        [[0, 5]]
        >>> solution([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        [[1, 2], [3, 10], [12, 16]]
        >>> solution([[1, 3], [6, 9]], [2, 5])
        [[1, 5], [6, 9]]
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


if __name__ == '__main__':
    doctest.testmod()
