import doctest


# ---------------------------------------------------------------------
# Approach 1: Count Ones. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Given a string s of zeros and ones, return the maximum score
    after splitting the string into two non-empty substrings. The score
    after splitting a string is the number of zeros in the left
    substring plus the number of ones in the right substring.

    Examples:
        >>> solution('1111')
        3
        >>> solution('00111')
        5
        >>> solution('011101')
        5
    """
    ones = s.count('1')
    zeros = score = 0
    for i in range(len(s) - 1):
        if s[i] == '0':
            zeros += 1
        else:
            ones -= 1
        score = max(score, zeros + ones)
    return score


if __name__ == '__main__':
    doctest.testmod()
