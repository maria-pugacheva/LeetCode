import doctest


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n)                               ***
# ---------------------------------------------------------------------
def solution_one(num: str) -> bool:
    """Return True if for every index i in the range 0 <= i < n, the
    digit i occurs num[i] times in num, otherwise return False.

    Preconditions:
        1 <= len(num) <= 10

    Examples:
        >>> solution_one('1210')
        True
        >>> solution_one('030')
        False
        >>> solution_one('121010908')
        False
    """
    d = {}
    for ch in num:
        d[int(ch)] = d.get(int(ch), 0) + 1
    for i in range(len(num)):
        if (i in d and d[i] != int(num[i])) or \
                (i not in d and int(num[i]) != 0):
            return False
    return True


# ---------------------------------------------------------------------
# Approach 2: Autobiographical Numbers. Time: O(1)                  ^**
# ---------------------------------------------------------------------
def solution_two(num: str) -> bool:
    """Return True if for every index i in the range 0 <= i < n, the
    digit i occurs num[i] times in num, otherwise return False.

    Preconditions:
        1 <= len(num) <= 10

    Examples:
        >>> solution_two('1210')
        True
        >>> solution_two('030')
        False
        >>> solution_two('121010908')
        False
    """
    if num in {'1210', '2020', '21200', '3211000', '42101000',
               '521001000', '6210001000'}:
        return True
    return False


if __name__ == '__main__':
    doctest.testmod()
