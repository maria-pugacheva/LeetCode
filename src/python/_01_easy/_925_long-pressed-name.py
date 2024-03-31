import doctest


# ---------------------------------------------------------------------
# Approach 1: Two Pointers. Time: O(n)                              ^**
# ---------------------------------------------------------------------
def solution(name: str, typed: str) -> bool:
    """Examine the typed characters of the keyboard and return True if
    it is possible that it was your friends name, with some characters
    (possibly none) being long pressed.

    Examples:
        >>> solution('alex', 'aaleex')
        True
        >>> solution('saeed', 'ssaaedd')
        False
        >>> solution('alex', 'aaleexa')
        False
        >>> solution('vtkgn', 'vttkgnn')
        True
        >>> solution('alex', 'ale')
        False
        >>> solution('pyplrz', 'ppyypllr')
        False
    """
    i = j = 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    return i == len(name)


if __name__ == '__main__':
    doctest.testmod()
