import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Count. Time: O(n)                                     ***
# ---------------------------------------------------------------------
def solution_one(widths: List[int], s: str) -> List[int]:
    """Return a list res where res[0] is the total number of lines
    needed to write string s (such that each line is no longer than
    100 pixels) and res[1] is the width of the last line in pixels.  The
    widths parameter denotes how many pixels wide each lowercase English
    letter is.

    Preconditions:
        len(widths) == 26
        2 <= widths[i] <= 10
        1 <= len(s) <= 1000
        s contains only lowercase English letters

    Examples:
        >>> solution_one([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'bbbcccdddaaa')
        [2, 4]
        >>> solution_one([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], 'abcdefghijklmnopqrstuvwxyz')
        [3, 60]
        >>> solution_one([2,5,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 'abc')
        [1, 10]
    """
    lines = 1
    cnt = 0
    for ch in s:
        w = widths[ord(ch) - 97]
        if cnt + w <= 100:
            cnt += w
        else:
            lines += 1
            cnt = w
    return [lines, cnt]


if __name__ == '__main__':
    doctest.testmod()
