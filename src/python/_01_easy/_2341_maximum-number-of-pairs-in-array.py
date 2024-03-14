import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(nums: List[int]) -> List[int]:
    """Return a list answer of size 2 where answer[0] is the number
    of pairs that can be found in nums and answer[1] is the number of
    leftover integers in nums after removing all the pairs from nums.

    Examples:
        >>> solution([0])
        [0, 1]
        >>> solution([1, 1])
        [1, 0]
        >>> solution([1, 3, 2, 1, 3, 2, 2])
        [3, 1]
    """
    s = set()
    cnt = 0
    for n in nums:
        if n in s:
            cnt += 1
            s.remove(n)
        else:
            s.add(n)
    return [cnt, len(s)]


if __name__ == '__main__':
    doctest.testmod()
