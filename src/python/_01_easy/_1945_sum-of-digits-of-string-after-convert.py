import doctest


# ---------------------------------------------------------------------
# Approach 1: Modulo                                                ***
# ---------------------------------------------------------------------
def solution(s: str, k: int) -> int:
    """Given a string s consisting of lowercase English letters, and an
    integer k, convert s into an integer by replacing each letter with
    its position in the alphabet (i.e., replace 'a' with 1). Then,
    transform the integer by replacing it with the sum of its digits.
    Repeat the transform operation k times in total.

    Preconditions:
        1 <= len(s) <= 100
        1 <= k <= 10
        s consists of lowercase English letters

    Examples:
        >>> solution('iiii', 1)
        36
        >>> solution('zbax', 2)
        8
        >>> solution('leetcode', 2)
        6
    """
    res = 0
    for ch in s:
        a = ord(ch) - 97 + 1
        res += a % 10 + a // 10
    while k > 1:
        t = 0
        while res:
            t += res % 10
            res //= 10
        res = t
        k -= 1
    return res


if __name__ == '__main__':
    doctest.testmod()
