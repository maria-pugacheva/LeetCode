import doctest


# ---------------------------------------------------------------------
# Approach 1: First Occurrence. Time: O(n). Space: O(N)             !!*
# ---------------------------------------------------------------------
def solution_one(a: str, b: str) -> bool:
    """Given two strings a and b, determine if they are isomorphic.

    Examples:
        >>> solution_one('egg', 'add')
        True
        >>> solution_one('foo', 'bar')
        False
        >>> solution_one('paper', 'title')
        True
        >>> solution_one('badc', 'baba')
        False
        >>> solution_one('bbbaaaba', 'aaabbbba')
        False
        >>> solution_one('13', '42')
        True
        >>> solution_one('abcdefghijklmnopqrstuvwxyzva', \
        'abcdefghijklmnopqrstuvwxyzck')
        False
    """
    def transform(s: str) -> str:
        indices, res = {}, []
        for i in range(len(s)):
            if s[i] not in indices:
                indices[s[i]] = str(i)
            res.append(indices[s[i]])
        # Add spaces to avoid cases as follows:
        # ..25210 == ..25210 (should be  ..25 21 0 != ..25 2 10)
        return ' '.join(res)  # See test case N7 above

    return transform(a) == transform(b)


# ---------------------------------------------------------------------
# Approach 2: Two HashMaps. Time: O(n). Space: O(1)                 ^**
# ---------------------------------------------------------------------
def solution_two(a: str, b: str) -> bool:
    """Given two strings a and b, determine if they are isomorphic.

    Examples:
        >>> solution_two('egg', 'add')
        True
        >>> solution_two('foo', 'bar')
        False
        >>> solution_two('paper', 'title')
        True
        >>> solution_two('badc', 'baba')
        False
        >>> solution_two('bbbaaaba', 'aaabbbba')
        False
        >>> solution_two('13', '42')
        True
    """
    map_s_t, map_t_s = {}, {}
    for i in range(len(a)):
        c1, c2 = a[i], b[i]
        if c1 not in map_s_t and c2 not in map_t_s:
            map_s_t[c1], map_t_s[c2] = c2, c1
        elif c1 not in map_s_t or c2 not in map_t_s or map_s_t[c1] != c2:
            return False
    return True


# ---------------------------------------------------------------------
# Approach 3: One HashMap. Time: O(n). Space: O(1)                  ***
# ---------------------------------------------------------------------
def solution_three(a: str, b: str) -> bool:
    """Given two strings a and b, determine if they are isomorphic.

    Examples:
        >>> solution_three('egg', 'add')
        True
        >>> solution_three('foo', 'bar')
        False
        >>> solution_three('paper', 'title')
        True
        >>> solution_three('badc', 'baba')
        False
        >>> solution_three('bbbaaaba', 'aaabbbba')
        False
        >>> solution_three('13', '42')
        True
        >>> solution_three('abcdefghijklmnopqrstuvwxyzva', \
        'abcdefghijklmnopqrstuvwxyzck')
        False
    """
    map_a_b = {}
    for i in range(len(a)):
        c1, c2 = 'a_' + a[i], 'b_' + b[i]
        if c1 not in map_a_b and c2 not in map_a_b:
            map_a_b[c1], map_a_b[c2] = i, i
        else:
            if c1 not in map_a_b:
                map_a_b[c1] = i
            elif c2 not in map_a_b:
                map_a_b[c2] = i
            if map_a_b[c1] != map_a_b[c2]:
                return False
    return True


if __name__ == '__main__':
    doctest.testmod()
