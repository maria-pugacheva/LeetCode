import doctest


# ---------------------------------------------------------------------
# Approach 1: One Pass. Time: O(n)                                  !**
# ---------------------------------------------------------------------
def solution(p: str) -> bool:
    """Given a password p, return True if it is a strong password. A
    password is said to be strong if it contains at least eight
    characters, at least one digit, at least one lower letter and one
    uppercase letter, and at least one special character.

    Examples:
        >>> solution('IloveLe3tcode!')
        True
        >>> solution('IloveLe3tcoode!')
        False
        >>> solution('1aB!')
        False
    """
    u = l = d = s = False
    for i in range(len(p)):
        if i > 0 and p[i] == p[i-1]:
            return False
        elif p[i].isupper():
            u = True
        elif p[i].islower():
            l = True
        elif p[i].isdigit():
            d = True
        else:
            s = True
    return len(p) >= 8 and u and l and d and s


if __name__ == '__main__':
    doctest.testmod()
