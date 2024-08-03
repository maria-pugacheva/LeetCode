import math
import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Math                                                    !
# ---------------------------------------------------------------------
def solution(area: int) -> List[int]:
    """Return [L, W] where L and W are the length and width of area.

    Notes:
        The width W should not be larger than the length L (L >= W).
        The difference between L and W should be as small as possible.

    Preconditions:
        1 <= area <= 10^7

    Examples:
        >>> solution(4)
        [2, 2]
        >>> solution(37)
        [37, 1]
        >>> solution(122122)
        [427, 286]
    """
    w = int(math.sqrt(area))
    while area % w != 0:
        w -= 1
    return [area // w, w]


if __name__ == '__main__':
    doctest.testmod()
