import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str, chars) -> int:
    """Return the number of words in s you can fully type using a
    keyboard that has broken keys chars.

    Preconditions:
        1 <= len(s) <= 10^4
        0 <= len(chars) <= 26
        s consists of words separated by a single space without any
            leading or trailing spaces (each word only consists of
            lowercase English letters)
        chars consists of distinct lowercase English letters

    Examples:
        >>> solution_one('my name is', 'ms')
        0
        >>> solution_one('i like this book', 'lt')
        2
        >>> solution_one('hello world i am', 'adi')
        1
    """
    broken = set(chars)
    can_type = True
    cnt = 0
    for ch in s:
        if ch in broken:
            can_type = False
        elif ch == ' ':
            if can_type:
                cnt += 1
            else:
                can_type = True
    return cnt + 1 if can_type else cnt


if __name__ == '__main__':
    doctest.testmod()
