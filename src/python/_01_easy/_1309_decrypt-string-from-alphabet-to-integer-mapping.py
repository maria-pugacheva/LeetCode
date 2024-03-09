import doctest


# ---------------------------------------------------------------------
# Approach 1: Ascii Values. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Map s to English lowercase characters as follows:
        - characters ('a' to 'i') are represented by ('1' to '9')
        - characters ('j' to 'z') are represented by ('10#' to '26#')

    Examples:
        >>> solution('1326#')
        'acz'
        >>> solution('10#11#12')
        'jkab'
        >>> solution('113#22#2397')
        'amvbcig'
    """
    res = []
    i = len(s) - 1
    while i >= 0:
        if s[i] == '#':
            res.insert(0, chr(96 + int(s[i-2:i])))
            i -= 3
        else:
            res.insert(0, chr(96 + int(s[i])))
            i -= 1
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
