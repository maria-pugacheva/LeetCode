import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n * m)                          ***
# ---------------------------------------------------------------------
def solution(words: List[str]) -> str:
    """Return the first palindromic string in words. If there is no
    such string, return an empty string ''.

    Examples:
        >>> solution(['def', 'ghi'])
        ''
        >>> solution(['notapalindrome', 'racecar'])
        'racecar'
        >>> solution(['abc', 'car', 'ada', 'racecar', 'cool'])
        'ada'
    """
    def is_palindrome(word: str) -> bool:
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True

    for w in words:
        if is_palindrome(w):
            return w
    return ''


if __name__ == '__main__':
    doctest.testmod()
