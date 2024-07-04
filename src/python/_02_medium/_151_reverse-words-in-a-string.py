import doctest


# ---------------------------------------------------------------------
# Approach 1: Built-In. Time: O(n). Space: O(n)                       ^
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Given an input string s, reverse the order of the words.

    Examples:
        >>> solution_one('the sky is blue')
        'blue is sky the'
        >>> solution_one('  hello world  ')
        'world hello'
        >>> solution_one('a good   example')
        'example good a'
    """
    return ' '.join(reversed(s.split()))


# ---------------------------------------------------------------------
# Approach 2: One Pass. Time: O(n). Space: O(n)                     ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> str:
    """Given an input string s, reverse the order of the words.

    Examples:
        >>> solution_two('the sky is blue')
        'blue is sky the'
        >>> solution_two('  hello world  ')
        'world hello'
        >>> solution_two('a good   example')
        'example good a'
    """
    res, end, seen_word = [], len(s) - 1, False
    for i in range(end, -1, -1):
        if s[i] != ' ' and not seen_word:
            seen_word = True
            end = i
        elif s[i] == ' ' and seen_word:
            seen_word = False
            res.append(s[i+1:end+1])
    if seen_word:
        res.append(s[:end+1])
    return ' '.join(res)


if __name__ == '__main__':
    doctest.testmod()
