import doctest


# ---------------------------------------------------------------------
# Approach 1: Stack. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Given a string s of lower and upper case English letters. A good
    string is a string which doesn't have two adjacent characters s[i]
    and s[i + 1] where s[i] is a lower-case letter and s[i + 1] is the
    same letter but in upper-case or vice-versa. Return the string after
    making it good.

    Preconditions:
        1 <= len(s) <= 100
        s contains only lower and upper case English letters

    Examples:
        >>> solution_one('')
        ''
        >>> solution_one('s')
        's'
        >>> solution_one('abBAcC')
        ''
        >>> solution_one('KaBbAg')
        'Kg'
        >>> solution_one('hHcOzoC')
        'cOzoC'
        >>> solution_one('leEeetcode')
        'leetcode'
    """
    stack = []
    for i in range(len(s)):
        if len(stack) > 0 and abs(ord(s[i]) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)


# ---------------------------------------------------------------------
# Approach 2: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> str:
    """Given a string s of lower and upper case English letters. A good
    string is a string which doesn't have two adjacent characters s[i]
    and s[i + 1] where s[i] is a lower-case letter and s[i + 1] is the
    same letter but in upper-case or vice-versa. Return the string after
    making it good.

    Preconditions:
        1 <= len(s) <= 100
        s contains only lower and upper case English letters

    Examples:
        >>> solution_two('')
        ''
        >>> solution_two('s')
        's'
        >>> solution_two('abBAcC')
        ''
        >>> solution_two('KaBbAg')
        'Kg'
        >>> solution_two('hHcOzoC')
        'cOzoC'
        >>> solution_two('leEeetcode')
        'leetcode'
    """
    s = list(s)
    end = 0
    for i in range(1, len(s)):
        if end >= 0 and abs(ord(s[i]) - ord(s[end])) == 32:
            end -= 1
        else:
            end += 1
            s[end] = s[i]
    return ''.join(s[:end + 1])


if __name__ == '__main__':
    doctest.testmod()
