import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(2*(n + m) + n log n)              ***
# ---------------------------------------------------------------------
def solution_one(a: List[List[int]], b: List[List[int]]) -> \
        List[List[int]]:
    """Given two 2D integer arrays, each array contains unique ids and
    is sorted in ascending order by id. Merge the two arrays into one
    array and return the resulting array. The returned array must be
    sorted in ascending order by id.

    Examples:
        >>> solution_one([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2]])
        [[1, 6], [2, 3], [3, 2], [4, 5]]
        >>> solution_one([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]])
        [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        >>> solution_one([[1, 1]], [[1, 2]])
        [[1, 3]]
    """
    d = {}
    for i in range(len(a)):
        d[a[i][0]] = a[i][1]
    for j in range(len(b)):
        d[b[j][0]] = d.get(b[j][0], 0) + b[j][1]
    res = []
    for k, v in d.items():
        res.append([k, v])
    res.sort()
    return res


# ---------------------------------------------------------------------
# Approach 2: Two Pointers. Time: O(n + m)                          ***
# ---------------------------------------------------------------------
def solution_two(a: List[List[int]], b: List[List[int]]) -> \
        List[List[int]]:
    """Given two 2D integer arrays, each array contains unique ids and
    is sorted in ascending order by id. Merge the two arrays into one
    array and return the resulting array. The returned array must be
    sorted in ascending order by id.

    Examples:
        >>> solution_two([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2]])
        [[1, 6], [2, 3], [3, 2], [4, 5]]
        >>> solution_two([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]])
        [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        >>> solution_two([[1, 1]], [[1, 2]])
        [[1, 3]]
    """
    res = []
    i = j = 0
    while i < len(a) or j < len(b):
        if i < len(a) and j < len(b):
            if a[i][0] == b[j][0]:
                res.append([a[i][0], a[i][1] + b[j][1]])
                i += 1
                j += 1
            elif a[i][0] < b[j][0]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        elif i < len(a):
            res.extend(a[i:])
            break
        else:
            res.extend(b[j:])
            break
    return res


if __name__ == '__main__':
    doctest.testmod()
