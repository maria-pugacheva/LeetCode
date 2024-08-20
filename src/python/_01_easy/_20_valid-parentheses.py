import doctest


# ---------------------------------------------------------------------
# Approach 1: Stack. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Given a string s containing just the characters '(', ')', '{',
    '}', '[', and ']', determine if the input string is valid.

    Examples:
        >>> solution_one('()')
        True
        >>> solution_one('(){}[]')
        True
        >>> solution_one('{[]}')
        True
        >>> solution_one('(({[]}))')
        True
        >>> solution_one('(}')
        False
        >>> solution_one('({[)')
        False
        >>> solution_one('(({[]}}}')
        False
    """
    valid = {'{}', '()', '[]'}
    stack = []
    for i in range(len(s)):
        if not stack or stack[-1] + s[i] not in valid:
            stack.append(s[i])
        else:
            stack.pop()
    return not stack


if __name__ == '__main__':
    doctest.testmod()
