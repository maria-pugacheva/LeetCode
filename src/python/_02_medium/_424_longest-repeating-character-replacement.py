import doctest


# ---------------------------------------------------------------------
# Approach 1: Sliding Window Optimized. Time: O(n). Space: O(m)       !
# ---------------------------------------------------------------------
# Complexity Analysis: This approach uses an auxiliary frequency map,
# with a space complexity of O(m) where m is the number of unique
# characters. For uppercase English letters, m is at most 26.
# ---------------------------------------------------------------------
def solution(s: str, k: int) -> int:
    """Given a string s and an integer k, where you can replace any
    character in the string with any other uppercase English character
    at most k times, return the length of the longest substring with the
    same letter after performing these operations.

    Examples:
        >>> solution('ABAB', 2)
        4
        >>> solution('AABABBA', 1)
        4
    """
    longest = 0
    charsFreq = {}
    maxFreq = 0
    i = 0
    for j, ch in enumerate(s):
        charsFreq[ch] = charsFreq.get(ch, 0) + 1
        maxFreq = max(maxFreq, charsFreq[ch])
        while (j - i + 1) - maxFreq > k:
            charsFreq[s[i]] -= 1
            i += 1
        longest = max(longest, j - i + 1)
    return longest


if __name__ == '__main__':
    doctest.testmod()
