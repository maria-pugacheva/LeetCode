import doctest


# ---------------------------------------------------------------------
# Approach 1: Brute Force. Time: O(n * m). Space: O(1)              ***
# ---------------------------------------------------------------------
# 1. Create a variable to keep track of all the stones occurring in the
#    jewels string, call it count.
# 2. Use nested loops to check whether each character of the stones
#    string appears in the jewels string.  If so, increment count.
# 3. Return the answer.
# ---------------------------------------------------------------------
def solution_one(stones: str, jewels: str) -> int:
    """Count how many of the stones you have are also jewels.

    Preconditions:
        stones consists of letters and have length at most 50
        jewels consists of distinct letters and have length at most 50
        letters in stones and jewels are case sensitive

    Examples:
        >>> solution_one('ZZ', 'z')
        0
        >>> solution_one('aAAbbbb', 'aA')
        3
    """
    count = 0
    for s in stones:
        for j in jewels:
            if s == j:
                count += 1
    return count


# ---------------------------------------------------------------------
# Approach 2: Set. Time: O(n + m). Space: O(m)                      ***
# ---------------------------------------------------------------------
# 1. Create a variable to keep track of all the stones occurring in the
#    jewels string, call it count.
# 2. Add the characters of the jewels string to a set.
# 3. Iterate through the characters of the stones string and check
#    whether each character of the stones string appears in the set.
#    If so, increment count.
# 4. Return the answer.
# ---------------------------------------------------------------------
def solution_two(stones: str, jewels: str) -> int:
    """Count how many of the stones you have are also jewels.

    Preconditions:
        stones consists of letters and have length at most 50
        jewels consists of distinct letters and have length at most 50
        letters in stones and jewels are case sensitive

    Examples:
        >>> solution_two('ZZ', 'z')
        0
        >>> solution_two('aAAbbbb', 'aA')
        3
    """
    count = 0
    j = set(jewels)
    for s in stones:
        if s in j:
            count += 1
    return count


if __name__ == '__main__':
    doctest.testmod()
