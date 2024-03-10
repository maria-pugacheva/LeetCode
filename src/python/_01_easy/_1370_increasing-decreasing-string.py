import doctest


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Reorder s.

    Examples:
        >>> solution('rat')
        'art'
        >>> solution('aaaabbbbcccc')
        'abccbaabccba'
    """
    chars = [0] * 26
    for ch in s:
        chars[ord(ch) - 97] += 1
    res = []
    cnt = len(s)
    while cnt > 0:
        for i in range(26):
            if chars[i] > 0:
                res.append(chr(i + 97))
                chars[i] -= 1
                cnt -= 1
                if cnt == 0:
                    break
        for j in range(25, -1, -1):
            if chars[j] > 0:
                res.append(chr(j + 97))
                chars[j] -= 1
                cnt -= 1
                if cnt == 0:
                    break
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
