import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Math. Time: O(n)                                      ***
# ---------------------------------------------------------------------
def solution(c: float) -> List[float]:
    """Convert Celsius c into Kelvin and Fahrenheit and return the
    values as an array ans = [kelvin, fahrenheit].

    Examples:
        >>> solution(36.50)
        [309.65, 97.7]
        >>> solution(122.11)
        [395.26, 251.798]
    """
    return [c + 273.15, c * 1.80 + 32.00]


if __name__ == '__main__':
    doctest.testmod()
