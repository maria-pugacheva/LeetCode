import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Return the number of '*' in s, excluding the '*' between each
    pair of '|'.

    Examples:
        >>> solution('l|*e*et|c**o|*de|')
        2
        >>> solution('iamprogrammer')
        0
        >>> solution('yo|uar|e**|b|e***au|tifu|l')
        5
    """
    cnt = pairs = 0
    for ch in s:
        if ch == '|':
            pairs += 1
        elif ch == '*' and pairs % 2 == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
