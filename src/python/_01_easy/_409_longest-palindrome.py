import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                         !
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the length of the longest palindrome that can be built
    with the letters in s.

    Preconditions:
        1 <= len(s) <= 2000
        s consists of lowercase and/or uppercase English letters only

    Examples:
        >>> solution_one('a')
        1
        >>> solution_one('bb')
        2
        >>> solution_one('abccccdd')
        7
    """
    cnt = 0
    chars = set()
    for ch in s:
        if ch in chars:
            chars.remove(ch)
            cnt += 2
        else:
            chars.add(ch)
    return cnt + 1 if len(chars) > 0 else cnt


if __name__ == '__main__':
    doctest.testmod()
