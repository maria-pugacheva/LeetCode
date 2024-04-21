import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sorting + Hash Map. Time: O(n log n)                  ***
# ---------------------------------------------------------------------
def solution(names: List[str], heights: List[int]) -> List[str]:
    """You are given an array of strings names, and an array heights
    that consists of distinct positive integers. Rearrange the people
    by their heights in a descending order.

    Examples:
        >>> solution(['Mary', 'John', 'Emma'], [180, 165, 170])
        ['Mary', 'Emma', 'John']
        >>> solution(['Alice', 'Bob', 'Bob'], [155, 185, 150])
        ['Bob', 'Alice', 'Bob']
        >>> solution(['Jo', 'Bob', 'Bob', 'Anna'], [180, 185, 150, 130])
        ['Bob', 'Jo', 'Bob', 'Anna']
    """
    d, res = {}, []
    for i in range(len(names)):
        d[heights[i]] = names[i]
    heights.sort(reverse=True)
    for h in heights:
        res.append(d[h])
    return res


if __name__ == '__main__':
    doctest.testmod()
