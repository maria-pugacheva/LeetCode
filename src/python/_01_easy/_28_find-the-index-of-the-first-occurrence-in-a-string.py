import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n * m). Space: O(1)             ***
# ---------------------------------------------------------------------
def solution_one(s: str, t: str) -> int:
    """Return the index of the 1st occurrence of t in s.

    Examples:
        >>> solution_one('k', 'k')
        0
        >>> solution_one('aa', 'b')
        -1
        >>> solution_one('hi', 'hey')
        -1
        >>> solution_one('hi', 'hii')
        -1
        >>> solution_one('hello', 'lo')
        3
        >>> solution_one('cccat', 'cat')
        2
    """
    len_s, len_t = len(s), len(t)
    for i in range(len_s - len_t + 1):
        if s[i] == t[0]:
            j = 0
            while j < len_t and s[i] == t[j]:
                i += 1
                j += 1
            if j == len_t:
                return i - len_t
    return -1


if __name__ == '__main__':
    doctest.testmod()
