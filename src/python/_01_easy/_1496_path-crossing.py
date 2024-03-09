import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                       ***
# ---------------------------------------------------------------------
def solution(path: str) -> bool:
    """Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each
    representing moving one unit north, south, east, or west. Return
    True if the path crosses itself at any point.

    Examples:
        >>> solution('SN')
        True
        >>> solution('WSSESEEE')
        False
        >>> solution('NEEEEEEEEEENNNNNNNNNNWWWWWWWWWW')
        False
    """
    s = set()
    s.add((0, 0))
    x = y = 0
    for p in path:
        if p == 'N':
            y += 1
        elif p == 'S':
            y -= 1
        elif p == 'E':
            x += 1
        else:
            x -= 1
        if (x, y) in s:
            return True
        s.add((x, y))
    return False


if __name__ == '__main__':
    doctest.testmod()
