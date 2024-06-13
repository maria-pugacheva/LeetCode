import doctest


# ---------------------------------------------------------------------
# Approach 1: Split. Time: O(n)                                     !**
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Given a string s consisting of words and spaces, return the
    length of the last word in the string.

    Examples:
        >>> solution_one('Hello World')
        5
        >>> solution_one('   fly me   to   the moon  ')
        4
        >>> solution_one('luffy is still joyboy')
        6
    """
    return len(s.strip().split()[-1])


# ---------------------------------------------------------------------
# Approach 2: One Pass. Time: O(n)                                  ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> int:
    """Given a string s consisting of words and spaces, return the
    length of the last word in the string.

    Examples:
        >>> solution_two('Hello World')
        5
        >>> solution_two('   fly me   to   the moon  ')
        4
        >>> solution_two('luffy is still joyboy')
        6
    """
    cnt = 0
    seen_alpha = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            cnt += 1
            seen_alpha = True
        elif seen_alpha:
            break
    return cnt


if __name__ == '__main__':
    doctest.testmod()
