import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> str:
    """Return s after reversing all the English letters in it.

    Preconditions:
        1 <= len(s) <= 100
        s consists of chars with ASCII values in the range [33, 122]
        s does not contain '\"' or '\\'

    Examples:
        >>> solution_one('-a')
        '-a'
        >>> solution_one('ab-cd')
        'dc-ba'
        >>> solution_one('Test1ng-Leet=code-Q!')
        'Qedo1ct-eeLg=ntse-T!'
    """
    chars = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        else:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
    return ''.join(chars)


if __name__ == '__main__':
    doctest.testmod()
