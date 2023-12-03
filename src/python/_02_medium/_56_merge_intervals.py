import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting. Time: O(nlog(n))                             ***
# ---------------------------------------------------------------------
def solution_one(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals and return an array of the
    non-overlapping intervals that cover all the intervals in the input.

       Examples:
           >>> solution_one([[1, 3], [2, 6], [8, 10], [15, 18]])
           [[1, 6], [8, 10], [15, 18]]
           >>> solution_one([[1, 4], [4, 5]])
           [[1, 5]]
           >>> solution_one([[1, 4], [2, 3]])
           [[1, 4]]
       """
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for i in range(1, len(intervals), 1):
        if res[-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            if intervals[i][1] > res[-1][1] >= intervals[i][0]:
                res[-1][1] = intervals[i][1]
    return res


if __name__ == '__main__':
    doctest.testmod()
