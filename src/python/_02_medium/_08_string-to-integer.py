import doctest


# ---------------------------------------------------------------------
# Approach 1: Follow the Rules                                        !
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Convert a string s to a 32-bit signed integer.

    Examples:
        >>> solution_one('42')
        42
        >>> solution_one(' -042')
        -42
        >>> solution_one('+-12')
        0
        >>> solution_one('1337c0d3')
        1337
        >>> solution_one('  +  413')
        0
        >>> solution_one('0-1')
        0
        >>> solution_one('words and 987')
        0
        >>> solution_one('-91283472332')
        -2147483648
        >>> solution_one('2147483649')
        2147483647
    """
    intMax, intMin = 2 ** 31 - 1, -2 ** 31
    res = 0
    sign = 1
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1

    if i < len(s) and s[i] == '-':
        sign = -1
        i += 1
    elif i < len(s) and s[i] == '+':
        i += 1

    while i < len(s) and s[i].isdigit():
        if res > intMax // 10 or (
                res == intMax // 10 and int(s[i]) > 7):
            return intMax if sign == 1 else intMin
        res = res * 10 + int(s[i])
        i += 1

    return res * sign


if __name__ == '__main__':
    doctest.testmod()
