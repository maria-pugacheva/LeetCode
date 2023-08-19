import doctest


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(s: str) -> int:
    """Given a string s representing an attendance record for a student,
    determine whether the student is eligible for an attendance award.

    Notes:
        The student is eligible for an attendance award if they meet
        both of the following criteria:
          1. The student was absent for no more than 1 day.
          2. The student was never late for 3 or more consecutive days.

    Preconditions:
        1 <= len(s) <= 1000
        s[i] is either 'A', 'L', or 'P'

    Examples:
        >>> solution_one('LLLALL')
        False
        >>> solution_one('PPALLP')
        True
        >>> solution_one('PAL')
        True
    """
    absent = late = 0
    for ch in s:
        if ch == 'L':
            late += 1
            if late == 3:
                return False
        else:
            if ch == 'A':
                absent += 1
            late = 0
    return absent < 2 and late < 3


if __name__ == '__main__':
    doctest.testmod()
