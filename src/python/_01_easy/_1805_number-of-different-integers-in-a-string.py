import doctest


# ---------------------------------------------------------------------
# Approach 1: Set. Time: O(n)                                        !!
# ---------------------------------------------------------------------
def solution(s: str) -> int:
    """Return the number of different integers in s.

    Preconditions:
        1 <= len(s) <= 1000
        s consists of digits and lowercase English letters

    Examples:
        >>> solution('a0a')
        1
        >>> solution('a00a')
        1
        >>> solution('a1b01c001bs0')
        2
        >>> solution('leet1234code234')
        2
        >>> solution('a123bc34d8ef34')
        3
    """
    nums = set()
    i = 0
    while i < len(s):
        if s[i].isdigit():
            while i < len(s) and s[i] == '0':
                i += 1
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            nums.add(s[i:j])
            i = j - 1
        i += 1
    return len(nums)


if __name__ == '__main__':
    doctest.testmod()
