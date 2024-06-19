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
        if len(stack) == 0 or stack[-1] + s[i] not in valid:
            stack.append(s[i])
        else:
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    doctest.testmod()
