import doctest


# ---------------------------------------------------------------------
# Approach 1: Frequency Count. Time: O(n)                           ***
# ---------------------------------------------------------------------
def solution_one(s: str, t: str) -> bool:
    """Return True if s and t are almost equivalent, or False otherwise.

    Notes:
        Two strings s and t of equal length are called almost equivalent
        if the number of occurrences of each letter from 'a' to 'z'
        between s and t differs by no more than 3.

    Preconditions:
        n == len(s) == len(t)
        1 <= n <= 100
        s and t consist only of lowercase English letters

    Examples:
        >>> solution_one('aaa', 'bcd')
        True
        >>> solution_one('abcdeef', 'abaaacc')
        True
        >>> solution_one('ccccddad', 'babababa')
        False
    """
    nums = [0] * 26
    for i in range(len(s)):
        nums[ord(s[i]) - 97] += 1
        nums[ord(t[i]) - 97] -= 1
    for n in nums:
        if n > 3 or n < -3:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
