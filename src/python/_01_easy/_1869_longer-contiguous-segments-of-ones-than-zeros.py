import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Given a binary string s, return True if the longest contiguous
    segment of 1's is strictly longer than the longest contiguous
    segment of 0's in s, or return False otherwise.

    Preconditions:
        1 <= len(s) <= 100
        s[i] is either '0' or '1'

    Examples:
        >>> solution_one('1101')
        True
        >>> solution_one('111000')
        False
        >>> solution_one('110100010')
        False
    """
    longest_ones = longest_zeros = ones = zeros = 0
    for ch in s:
        if ch == '1':
            ones += 1
            longest_ones = max(longest_ones, ones)
            zeros = 0
        else:
            zeros += 1
            longest_zeros = max(longest_zeros, zeros)
            ones = 0
    return longest_ones > longest_zeros


if __name__ == '__main__':
    doctest.testmod()
