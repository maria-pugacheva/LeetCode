import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  !**
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Given a string s consisting of words and spaces, return the
    length of the last word in the string.

    Examples:
        >>> solution('Hello World')
        5
        >>> solution('   fly me   to   the moon  ')
        4
        >>> solution('luffy is still joyboy')
        6
    """
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            cnt += 1
        elif cnt > 0:
            break
    return cnt


if __name__ == '__main__':
    doctest.testmod()
