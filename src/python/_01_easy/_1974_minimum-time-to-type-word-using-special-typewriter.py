import doctest


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                    !**
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the minimum number of seconds to type out the chars in s.

    Notes:
        Each second, you may perform one of the following operations:
            - Move the pointer one char counterclockwise or clockwise;
            - Type the char the pointer is currently on.

    Preconditions:
        1 <= len(s) <= 100
        s consists of lowercase English letters

    Examples:
        >>> solution_one('a')
        1
        >>> solution_one('b')
        2
        >>> solution_one('abz')
        6
        >>> solution_one('bza')
        7
        >>> solution_one('zjpc')
        34
    """
    cnt, prev = len(s), 'a'
    for ch in s:
        val = abs(ord(ch) - ord(prev))
        cnt += min(val, 26 - val)
        prev = ch
    return cnt


if __name__ == '__main__':
    doctest.testmod()
