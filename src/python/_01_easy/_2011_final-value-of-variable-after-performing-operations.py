import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Iterative. Time: O(n)                                 ***
# ---------------------------------------------------------------------
def solution_one(operations: List[str]) -> int:
    """Return the final value of N after performing all the operations.

    Notes:
        There is a programming language with only four operations and
        one variable N (initially, the value of N is 0):

            ++N and N++ increments the value of the variable N by 1.
            --N and N-- decrements the value of the variable N by 1.

    Preconditions:
        1 <= len(operations) <= 100
        operations[i] will be either '++N', 'N++', '--N', or 'N--'

    Examples:
        >>> solution_one(['--N'])
        -1
        >>> solution_one(['--N','N++'])
        0
        >>> solution_one(['--N','N++','N++'])
        1
    """
    n = 0
    for op in operations:
        if op[0] == '+' or op[-1] == '+':
            n += 1
        else:
            n -= 1
    return n


if __name__ == '__main__':
    doctest.testmod()
