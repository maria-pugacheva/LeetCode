import doctest


# ---------------------------------------------------------------------
# Approach 1: Left-To-Right. Time: O(1)                             ^**
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Given a roman numeral s, convert it to an integer.

    Examples:
        >>> solution('III')
        3
        >>> solution('LVIII')
        58
        >>> solution('MCMXCIV')
        1994
    """
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = nums[s[-1]]
    for i in range(len(s) - 1):
        if nums[s[i]] < nums[s[i + 1]]:
            n -= nums[s[i]]
        else:
            n += nums[s[i]]
    return n


if __name__ == '__main__':
    doctest.testmod()
