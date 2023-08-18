import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pointer. Time: O(n + m)                           ***
# ---------------------------------------------------------------------
def solution(s: str, t: str) -> str:
    """Merge the strings s and t in alternating order.

    Preconditions:
        1 <= len(s), len(t) <= 100
        s and t consist of lowercase English letters

    Examples:
        >>> solution('ab', 'pqrs')
        'apbqrs'
        >>> solution('abc', 'pqr')
        'apbqcr'
        >>> solution('abcd', 'pq')
        'apbqcd'
    """
    res = []
    i = 0
    while i < len(s) or i < len(t):
        if i < len(s):
            res.append(s[i])
        if i < len(t):
            res.append(t[i])
        i += 1
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
