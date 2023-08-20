import doctest


# ---------------------------------------------------------------------
# Approach 1: Helper Function. Time: O(n + m + t)                   ***
# ---------------------------------------------------------------------
def solution_one(firstWord: str, secondWord: str, target: str) -> int:
    """Determine if the summation of the numerical values of firstWord
    and secondWord equals the numerical value of target.

    Preconditions:
        1 <= firstWord.length, secondWord.length, target.length <= 8
        firstWord, secondWord, and target consist of lowercase English
            letters from 'a' to 'j' inclusive

    Examples:
        >>> solution_one('acb', 'cba', 'cdb')
        True
        >>> solution_one('aaa', 'a', 'aab')
        False
        >>> solution_one('aaa', 'aa', 'aaaa')
        True
    """
    def helper(s: str) -> int:
        n = 0
        for ch in s:
            n = n * 10 + (ord(ch) - 97)
        return n

    return helper(firstWord) + helper(secondWord) == helper(target)


if __name__ == '__main__':
    doctest.testmod()
