import doctest


# ---------------------------------------------------------------------
# Approach 1: Counting Chars. Time: O(n)                            ^**
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the maximum number of instances of the word 'balloon' that
    can be formed using the characters in s.

    Preconditions:
        1 <= len(s) <= 10^4
        s consists of lowercase English letters only

    Examples:
        >>> solution_one('ballon')
        0
        >>> solution_one('leetcode')
        0
        >>> solution_one('loonbalxballpoon')
        2
    """
    cnt = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    for ch in s:
        if ch in cnt:
            cnt[ch] += 1
    return min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])


# ---------------------------------------------------------------------
# Approach 2: Universal Solution. Time: O(n + m)                    ***
# ---------------------------------------------------------------------
def solution_two(s: str) -> int:
    """Return the maximum number of instances of the word 'balloon' that
    can be formed using the characters in s.

    Preconditions:
        1 <= len(s) <= 10^4
        s consists of lowercase English letters only

    Examples:
        >>> solution_two('ballon')
        0
        >>> solution_two('leetcode')
        0
        >>> solution_two('loonbalxballpoon')
        2
    """
    word = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    ht = {}
    for ch in s:
        if ch in word:
            ht[ch] = ht.get(ch, 0) + 1

    cnt = 10000
    for k, v in word.items():
        if k not in ht:
            return 0
        cnt = min(cnt, ht[k] // v)

    return cnt


if __name__ == '__main__':
    doctest.testmod()
