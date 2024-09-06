import doctest


# ---------------------------------------------------------------------
# Approach 1: Sliding Window. T: O(l1 + (l2 − l1)). S: O(1)           !
# ---------------------------------------------------------------------
# Complexity Analysis: Let l1 be the length of string s1 and l2 be the
# length of string s2
# ---------------------------------------------------------------------
def solution(s1: str, s2: str) -> bool:
    """Given two strings s1 and s2, return True if one of s1's
    permutations is the substring of s2.

    Examples:
        >>> solution('adc', 'dcda')
        True
        >>> solution('ab', 'eidbaooo')
        True
        >>> solution('ab', 'eidboaoo')
        False
        >>> solution('abc', 'bbbca')
        True
        >>> solution('hello', 'ooolleoooleh')
        False
        >>> solution('abc', 'cccccbabbbaaaa')
        True
    """
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - 97] += 1
        s2Count[ord(s2[i]) - 97] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        indLeft = ord(s2[l]) - 97
        s2Count[indLeft] -= 1
        if s1Count[indLeft] == s2Count[indLeft]:
            matches += 1
        elif s1Count[indLeft] == s2Count[indLeft] + 1:
            matches -= 1

        indRight = ord(s2[r]) - 97
        s2Count[indRight] += 1
        if s1Count[indRight] == s2Count[indRight]:
            matches += 1
        elif s1Count[indRight] == s2Count[indRight] - 1:
            matches -= 1

        l += 1

    return matches == 26


if __name__ == '__main__':
    doctest.testmod()
