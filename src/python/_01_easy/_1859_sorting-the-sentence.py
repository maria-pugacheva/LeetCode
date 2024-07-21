import doctest


# ---------------------------------------------------------------------
# Approach 1: Split and Slice                                         !
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Given a shuffled sentence s, return the original sentence.

    Preconditions:
        2 <= len(s) <= 200
        s consists of English letters, spaces, and digits from 1 to 9
            (the number of words in s is between 1 and 9)
        s contains no leading or trailing spaces

    Examples:
        >>> solution('am2 I1')
        'I am'
        >>> solution('Myself2 Me1 I4 and3')
        'Me Myself and I'
        >>> solution('is2 sentence4 This1 a3')
        'This is a sentence'
    """
    words = s.split()
    res = [''] * len(words)
    for w in words:
        res[int(w[-1]) - 1] = w[:-1]
    return ' '.join(res)


if __name__ == '__main__':
    doctest.testmod()
