import doctest


# ---------------------------------------------------------------------
# Approach 1: DP. T: O(m*n), dp arr of size n is filled m times       !
# ---------------------------------------------------------------------
def solution(s1: str, s2: str, s3: str) -> bool:
    """Given strings s1, s2, and s3, find whether s3 is formed by an
    interleaving of s1 and s2.

    Examples:
        >>> solution('', '', '')
        True
        >>> solution('aabcc', 'dbbca', 'aadbbcbcac')
        True
        >>> solution('aabcc', 'dbbca', 'aadbbbaccc')
        False
    """
    if len(s3) != len(s1) + len(s2):
        return False
    dp = [False] * (len(s2) + 1)
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 and j == 0:
                dp[j] = True
            elif i == 0:
                dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
            elif j == 0:
                dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
            else:
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                )
    return dp[len(s2)]


if __name__ == '__main__':
    doctest.testmod()
