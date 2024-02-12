import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(words: List[str], x: str) -> List[int]:
    """Return an array of indices representing the words that contain
    the character x.

    Examples:
        >>> solution_one(['hello', 'world'], 'l')
        [0, 1]
        >>> solution_one(['abc', 'bcd', 'aaaa', 'cbc'], 'a')
        [0, 2]
    """
    res = []
    for i in range(len(words)):
        for ch in words[i]:
            if ch == x:
                res.append(i)
                break
    return res


if __name__ == '__main__':
    doctest.testmod()
