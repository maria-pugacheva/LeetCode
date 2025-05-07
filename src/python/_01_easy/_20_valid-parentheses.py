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
    pairs = {'}': '{', ')': '(', ']': '['}
    stack = []
    for ch in s:
        if ch not in pairs:
            stack.append(ch)
        else:
            top_elem = stack.pop() if stack else '#'
            if top_elem != pairs[ch]:
                return False
    return not stack


if __name__ == '__main__':
    doctest.testmod()
