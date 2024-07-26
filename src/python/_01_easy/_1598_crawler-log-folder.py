import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution(logs: List[str]) -> int:
    """Return the minimum number of operations needed to go back to the
    main folder after the change folder operations in logs.

    Notes:
        "../" : Move to the parent folder of the current folder. If you
        are already in the main folder, remain in the same folder.
        "./" : Remain in the same folder.
        "x/" : Move to the child folder named x.

    Preconditions:
        1 <= len(logs) <= 10^3
        2 <= len(logs[i]) <= 10
        logs[i] contains lowercase English letters, digits, '.', and '/'
        logs[i] follows the format described in the statement

    Examples:
        >>> solution(['d1/', '../', '../', '../'])
        0
        >>> solution(['d1/', 'd2/', '../', 'd21/', './'])
        2
        >>> solution(['d1/', 'd2/', './', 'd3/', '../', 'd31/'])
        3
    """
    cnt = 0
    for log in logs:
        if log[0].isalnum():
            cnt += 1
        elif log == '../' and cnt > 0:
            cnt -= 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
