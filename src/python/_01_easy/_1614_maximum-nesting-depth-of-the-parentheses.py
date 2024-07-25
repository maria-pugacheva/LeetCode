import doctest


# ---------------------------------------------------------------------
# Approach 1: Parentheses Balance. Time: O(n)                       !**
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the nesting depth of s.

    Preconditions:
        1 <= len(s) <= 100
        s consists of digits 0-9 and chars '+', '-', '*', '/', '(', ')'
        s is a valid parentheses string

    Examples:
        >>> solution_one('1')
        0
        >>> solution_one('1+(2*3)/(2-1)')
        1
        >>> solution_one('(1)+((2))+(((3)))')
        3
    """
    max_depth = depth = 0
    for ch in s:
        if ch == '(':
            depth += 1
            max_depth = max(depth, max_depth)
        elif ch == ')':
            depth -= 1
    return max_depth


if __name__ == '__main__':
    doctest.testmod()
