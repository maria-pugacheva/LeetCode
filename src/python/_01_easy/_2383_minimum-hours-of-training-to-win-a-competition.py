import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                    !**
# ---------------------------------------------------------------------
def solution(initEnergy: int, initExp: int, energy: List[int], exp: List[int]) -> int:
    """You will face n opponents in order. The energy and experience of
    the i-th opponent is denoted by energy[i] and exp[i] respectively.
    When you face an opponent, you need to have both strictly greater
    experience and energy to defeat them. Before starting the
    competition, you can train for some number of hours. Return the
    minimum number of training hours required to defeat all n opponents.

    Examples:
        >>> solution(1, 1, [1, 1, 1, 1], [1, 1, 1, 50])
        51
        >>> solution(5, 3, [1, 4, 3, 2], [2, 6, 3, 1])
        8
        >>> solution(2, 4, [1], [3])
        0
    """
    hours = 0
    for i in range(len(energy)):
        if initEnergy <= energy[i]:
            a = energy[i] - initEnergy + 1
            hours += a
            initEnergy += a
        if initExp <= exp[i]:
            b = exp[i] - initExp + 1
            hours += b
            initExp += b
        initEnergy -= energy[i]
        initExp += exp[i]
    return hours


if __name__ == '__main__':
    doctest.testmod()
