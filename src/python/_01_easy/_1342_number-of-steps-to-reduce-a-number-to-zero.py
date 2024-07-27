import doctest


# ---------------------------------------------------------------------
# Approach 1: Simulation. Time: O(log n)                            ***
# ---------------------------------------------------------------------
def solution_one(num: int) -> int:
    """Return the number of steps to reduce num to zero. In one step,
    if the current number is even, you have to divide it by 2;
    otherwise, you have to subtract 1 from it.

    Preconditions:
        0 <= n <= 10^6

    Examples:
        >>> solution_one(0)
        0
        >>> solution_one(8)
        4
        >>> solution_one(123)
        12
    """
    cnt = 0
    while num:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        cnt += 1
    return cnt


# ---------------------------------------------------------------------
# Approach 2: Bit Manipulation                                      ^**
# ---------------------------------------------------------------------
# Hint: If we subtract 1 from an odd number, the last bit of the number
#       changes from 1 to 0. Dividing the number by 2 removes the last
#       bit from the number.
# ---------------------------------------------------------------------
def solution_two(num: int) -> int:
    """Return the number of steps to reduce num to zero. In one step,
    if the current number is even, you have to divide it by 2;
    otherwise, you have to subtract 1 from it.

    Preconditions:
        0 <= n <= 10^6

    Examples:
        >>> solution_two(0)
        0
        >>> solution_two(8)
        4
        >>> solution_two(123)
        12
    """
    if num == 0:
        return 0
    cnt, n = 0, bin(num)
    for i in range(len(n) - 1, 1, -1):
        if n[i] == '1' and i != 2:
            cnt += 1
        cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
