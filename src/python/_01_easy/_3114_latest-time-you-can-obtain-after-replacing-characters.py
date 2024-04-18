import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(1)                                  ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Replace all the '?' characters in s with digits such that the
    time we obtain by the resulting string is a valid 12-hour format
    time and is the latest possible.

    Examples:
        >>> solution('1?:?4')
        '11:54'
        >>> solution('0?:5?')
        '09:59'
        >>> solution('??:??')
        '11:59'
        >>> solution('??:1?')
        '11:19'
        >>> solution('?9:5?')
        '09:59'
        >>> solution('?0:40')
        '10:40'
    """
    res = list(s)
    if s[0] == '?':
        res[0] = '1' if s[1] in {'0', '1', '?'} else '0'
    if s[1] == '?':
        res[1] = '1' if res[0] == '1' else '9'
    if s[3] == '?':
        res[3] = '5'
    if s[4] == '?':
        res[4] = '9'
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
