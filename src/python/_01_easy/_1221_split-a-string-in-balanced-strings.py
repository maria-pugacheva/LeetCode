import doctest


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n). Space: O(1)                       ***
# ---------------------------------------------------------------------
def solution_one(string: str) -> int:
    """Return the maximum number of strings that are balanced in string.

    Notes:
        A balanced string is a string that has an equal amount of the
        following two characters: 'L' and 'R'.  Example: 'LLRRLR'.

    Preconditions:
        1 <= len(string) <= 1000
        string[i] = 'L' or 'R'
        string is balanced

    Examples:
        >>> solution_one('L')
        0
        >>> solution_one('LLLLRRRR')
        1
        >>> solution_one('RLRRRLLRLL')
        2
        >>> solution_one('RLLLLRRRLR')
        3
        >>> solution_one('RLRRLLRLRL')
        4
    """
    cnt = 0
    balance = 0
    for ch in string:
        if ch == 'L':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
