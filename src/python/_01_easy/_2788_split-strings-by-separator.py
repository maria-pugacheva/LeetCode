import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Split Manually                                        ***
# ---------------------------------------------------------------------
def solution(words: List[str], separator: str) -> List[str]:
    """Given a list of strings words and a character separator, split
    each string in words by separator. Return a list of strings
    containing the new strings formed, excluding empty strings.

    Examples:
        >>> solution(['|||'], '|')
        []
        >>> solution(['$easy$', '$problem$'], '$')
        ['easy', 'problem']
        >>> solution(['one.two.three', 'four.five', 'six'], '.')
        ['one', 'two', 'three', 'four', 'five', 'six']
    """
    res = []
    for w in words:
        prev = 0
        for i in range(len(w)):
            if w[i] == separator:
                if i - prev > 0:
                    res.append(w[prev:i])
                prev = i + 1
            else:
                if i == len(w) - 1:
                    res.append(w[prev:i+1])
    return res


if __name__ == '__main__':
    doctest.testmod()
