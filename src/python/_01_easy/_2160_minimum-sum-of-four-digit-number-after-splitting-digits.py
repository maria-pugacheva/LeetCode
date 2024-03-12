import doctest


# ---------------------------------------------------------------------
# Approach 1: Sorting                                               ***
# ---------------------------------------------------------------------
def solution(num: int) -> int:
    """Split num into two new integers new1 and new2 and return the
    minimum possible sum of new1 and new2.

    Examples:
        >>> solution(2932)
        52
        >>> solution(4008)
        12
    """
    nums = []
    while num:
        nums.append(num % 10)
        num = num // 10
    nums.sort()
    return (nums[0] + nums[1]) * 10 + nums[2] + nums[3]


if __name__ == '__main__':
    doctest.testmod()
