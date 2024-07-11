import doctest


# ---------------------------------------------------------------------
# Approach 1: Map. Time: O(1)                                         !
# ---------------------------------------------------------------------
def solution(num: int) -> str:
    """Given an integer, convert it to a Roman numeral.

    Examples:
        >>> solution(3749)
        'MMMDCCXLIX'
        >>> solution(58)
        'LVIII'
        >>> solution(1994)
        'MCMXCIV'
    """
    digits = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    res = []
    for pair in digits:
        if num == 0:
            break
        res.append(pair[1] * (num // pair[0]))
        num %= pair[0]
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
