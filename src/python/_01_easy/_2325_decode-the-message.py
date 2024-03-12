import doctest


# ---------------------------------------------------------------------
# Approach 1: Dictionary. Time: O(n)                                ***
# ---------------------------------------------------------------------
def solution(key: str, message: str) -> str:
    """Decode message.

    Examples:
        >>> solution('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv')
        'this is a secret'
        >>> solution('eljuxhpwnyrdgtqkviszcfmabo', 'zwx hnfx lqantp')
        'the five boxing'
    """
    cnt = 1
    d = {}
    for ch in key:
        if cnt < 27:
            if ch.isalpha() and ch not in d:
                d[ch] = chr(cnt + 96)
                cnt += 1
        else:
            break
    res = list(message)
    for i in range(len(message)):
        if res[i] != ' ':
            res[i] = d[res[i]]
    return ''.join(res)


if __name__ == '__main__':
    doctest.testmod()
