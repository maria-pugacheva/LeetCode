import doctest


# ---------------------------------------------------------------------
# Approach 1: Conditions. Time: O(1)                                ***
# ---------------------------------------------------------------------
def solution(nOnes: int, nZeros: int, nNegOnes: int, k: int) -> int:
    """There is a bag that consists of items, each item has a number 1,
    0, or -1 written on it. Pick exactly k items among the available
    items. Return the maximum possible sum of numbers written on the
    items.

    Examples:
        >>> solution(3, 2, 0, 2)
        2
        >>> solution(3, 2, 0, 4)
        3
    """
    if k < nOnes:
        return k
    elif k <= nOnes + nZeros:
        return nOnes
    return nOnes - (k - nOnes - nZeros)


if __name__ == '__main__':
    doctest.testmod()
