import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(1)*                                      ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Given a string s consisting of lowercase English letters, return
    the first letter to appear twice.

    Notes:
        *The time complexity is O(1) because the loop will run till
        there's a repetition, and a repetition HAS to occur on or
        before the 27th iteration - there can not exist a string with
        more than 26 unique characters.

    Examples:
        >>> solution('aa')
        'a'
        >>> solution('abcdd')
        'd'
        >>> solution('abccbaacz')
        'c'
    """
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return ''


if __name__ == '__main__':
    doctest.testmod()
