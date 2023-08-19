import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str, k: int) -> str:
    """Return s such that it contains only the first k​words.

    Preconditions:
        1 <= len(s) <= 500
        k is in the range [1, the number of words in s]
        s consist of only English letters and spaces

    Examples:
        >>> solution_one('I am happy', 3)
        'I am happy'
        >>> solution_one('Hello how are you Contestant', 4)
        'Hello how are you'
        >>> solution_one('What is the solution to this problem', 4)
        'What is the solution'
    """
    for i in range(len(s)):
        if s[i] == ' ':
            k -= 1
        if k == 0:
            return s[:i]
    return s


if __name__ == '__main__':
    doctest.testmod()
