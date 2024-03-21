import doctest


# ---------------------------------------------------------------------
# Approach 1: Compare Three Values at a Time. Time: O(n)            ***
# ---------------------------------------------------------------------
def solution(num: str) -> str:
    """Given a string num representing a large integer, return the
    maximum good integer as a string or an empty string "" if no such
    integer exists. An integer is good if is a substring of num with
    length 3 and it consists of only one unique digit.

    Examples:
        >>> solution('42352338')
        ''
        >>> solution('2300019')
        '000'
        >>> solution('613337779')
        '777'
    """
    res = ''
    for i in range(1, len(num) - 1):
        if num[i - 1] == num[i] == num[i + 1]:
            res = max(res, num[i - 1:i + 2])
    return res


if __name__ == '__main__':
    doctest.testmod()
