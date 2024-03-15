import doctest


# ---------------------------------------------------------------------
# Approach 1: Sliding Window. Time: O(n * 26) -> O(n)               ***
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Return the number of good substrings of length three in s.
    A string is good if there are no repeated characters.​​​​

    Examples:
        >>> solution('ab')
        0
        >>> solution('xyzzaz')
        1
        >>> solution('aababcabc')
        4
    """
    seen = [0] * 26
    cnt = 0
    for i in range(len(s)):
        seen[ord(s[i]) - 97] += 1
        if i > 2:
            seen[ord(s[i-3]) - 97] -= 1
        if seen.count(1) == 3:
            cnt += 1
    return cnt


if __name__ == '__main__':
    doctest.testmod()
