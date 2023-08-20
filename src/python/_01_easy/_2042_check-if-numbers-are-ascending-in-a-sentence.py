import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Given a string s representing a sentence, check if all the
    numbers in s are strictly increasing from left to right.

    Preconditions:
        3 <= len(s) <= 200
        s consists of lowercase English letters, spaces, and digits
            from 0 to 9, inclusive
        the number of tokens in s is between 2 and 100, inclusive
        the tokens in s are separated by a single space
        there are at least two numbers in s
        each number in s is a positive number less than 100, with no
            leading zeros
        s contains no leading or trailing spaces

    Examples:
        >>> solution_one('1 box has 3 blue 4 red 6 green 12 yellow')
        True
        >>> solution_one('hi 5 x 5')
        False
        >>> solution_one('sunset is at 7 51 pm in the low 50 and 60 s')
        False
    """
    curr = i = 0
    while i < len(s):
        if s[i].isdigit():
            n = 0
            while i < len(s) and s[i] != ' ':
                n = n * 10 + int(s[i])
                i += 1
            if n <= curr:
                return False
            curr = n
        i += 1
    return True


if __name__ == '__main__':
    doctest.testmod()
