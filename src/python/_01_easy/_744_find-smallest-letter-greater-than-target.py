import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(letters: List[str], target) -> str:
    """Return the smallest character in letters that is
    lexicographically greater than target.  If such a character does not
    exist, return the first character in letters.

    Preconditions:
        2 <= len(letters) <= 10^4
        letters[i] is a lowercase English letter
        letters is sorted in non-decreasing order
        letters contains at least two different characters
        target is a lowercase English letter

    Examples:
        >>> solution_one(['c', 'f', 'j'], 'a')
        'c'
        >>> solution_one(['c', 'f', 'j'], 'c')
        'f'
        >>> solution_one(['a', 'a', 'b', 'c'], 'd')
        'a'
    """
    for ch in letters:
        if ord(ch) > ord(target):
            return ch
    return letters[0]


if __name__ == '__main__':
    doctest.testmod()
