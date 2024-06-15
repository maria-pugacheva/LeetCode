import doctest


# ---------------------------------------------------------------------
# Approach 1: Two HashMaps. Time: O(n + m). Space: O(n)             ***
# ---------------------------------------------------------------------
def solution_one(p: str, words: str) -> bool:
    """Given a pattern and a string s, find if s follows the same
    pattern.

    Examples:
        >>> solution_one('abba', 'dog cat cat dog')
        True
        >>> solution_one('abba', 'dog cat cat fish')
        False
        >>> solution_one('aaaa', 'dog cat cat dog')
        False
        >>> solution_one('aaa', 'aa aa aa')
        True
        >>> solution_one('aaa', 'aa aa aa aa')
        False
    """
    map_p_s, map_s_p = {}, {}
    s = words.split()
    if len(p) != len(s):
        return False
    for i in range(len(p)):
        c1, c2 = p[i], s[i]
        if c1 not in map_p_s and c2 not in map_s_p:
            map_p_s[c1], map_s_p[c2] = c2, c1
        elif c1 not in map_p_s or c2 not in map_s_p or map_p_s[c1] != c2:
            return False
    return True


# ---------------------------------------------------------------------
# Approach 2: One HashMap. Time: O(n + m). Space: O(n)              ***
# ---------------------------------------------------------------------
def solution_two(p: str, words: str) -> bool:
    """Given a pattern and a string s, find if s follows the same
    pattern.

    Examples:
        >>> solution_two('abba', 'dog cat cat dog')
        True
        >>> solution_two('abba', 'dog cat cat fish')
        False
        >>> solution_two('aaaa', 'dog cat cat dog')
        False
        >>> solution_two('aaa', 'aa aa aa')
        True
        >>> solution_two('aaa', 'aa aa aa aa')
        False
    """
    map_p_s = {}
    s = words.split()
    if len(p) != len(s):
        return False
    for i in range(len(p)):
        c1, c2 = 'p_' + p[i], 's_' + s[i]
        if c1 not in map_p_s:
            map_p_s[c1] = i
        if c2 not in map_p_s:
            map_p_s[c2] = i
        if map_p_s[c1] != map_p_s[c2]:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
