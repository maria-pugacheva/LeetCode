import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Stack. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(record: List[str]) -> int:
    """Return the sum of all the scores on the record record.

    Notes:
        At the beginning of the game, you start with an empty record.
        You are given a list of strings record, where record[i] is the
        ith operation you must apply to the record and is one of the
        following:
            - An integer x - Record a new score of x.
            - '+' - Record a new score that is the sum of the previous
              two scores.
            - 'D' - Record a new score that is double the previous one.
            - 'C' - Invalidate the previous score, removing it from the
              record.
        It is guaranteed record[i] is always valid.

    Preconditions:
        1 <= len(record) <= 1000

    Examples:
        >>> solution_one(['1'])
        1
        >>> solution_one(['5', '2', 'C', 'D', '+'])
        30
        >>> solution_one(['5', '-2', '4', 'C', 'D', '9', '+', '+'])
        27
    """
    res = []
    for item in record:
        if item == 'C':
            res.pop()
        elif item == 'D':
            res.append(res[-1] * 2)
        elif item == '+':
            res.append(res[-1] + res[-2])
        else:
            res.append(int(item))
    return sum(res)


if __name__ == '__main__':
    doctest.testmod()
