import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Given a string s, return True if, after converting all uppercase
    letters into lowercase letters and removing all non-alphanumeric
    characters, it is a palindrome. Otherwise, return False.

    Examples:
        >>> solution_one(' ')
        True
        >>> solution_one('race a car')
        False
        >>> solution_one('A man, a plan, a canal: Panama')
        True
    """
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


if __name__ == '__main__':
    doctest.testmod()
