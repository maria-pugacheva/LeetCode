import doctest


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                       !
# ---------------------------------------------------------------------
def solution_one(s: str) -> bool:
    """Return True if Alice wins, or return False if Bob wins.

       Preconditions:
           len(haystack) > 0
           haystack contains only lowercase English letters
           needle contains only lowercase English letters

       Examples:
           >>> solution_one('AA')
           False
           >>> solution_one('BBAAABBABBABB')
           True
           >>> solution_one('AAABABB')
           True
       """
    a = b = 0
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i] == s[i + 1]:
            if s[i] == 'A':
                a += 1
            else:
                b += 1
    return a > b


if __name__ == '__main__':
    doctest.testmod()
