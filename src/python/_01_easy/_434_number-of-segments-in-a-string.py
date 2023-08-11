import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Return the number of sequences of non-space characters in s.

    Preconditions:
        <= len(s) <= 300
        s consists of lower and uppercase English letters, digits, one
            of the following chars "!@#$%^&*()_+-=',.:", and spaces.

    Examples:
        >>> solution_one('  ')
        0
        >>> solution_one('Hello')
        1
        >>> solution_one('Hi, my    name is John. ')
        5
    """
    cnt = 0
    flag = False
    for ch in s:
        if ch == ' ':
            if flag:
                cnt += 1
                flag = False
        else:
            flag = True
    return cnt + 1 if flag else cnt


if __name__ == '__main__':
    doctest.testmod()
