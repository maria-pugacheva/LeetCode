import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Greedy. Time: O(n)                                    ***
# ---------------------------------------------------------------------
def solution_one(bills: List[int]) -> bool:
    """Given a list of integers bills where bills[i] is the bill the ith
    customer pays, return True if it is possible to provide every
    customer with correct change, or False otherwise.

    Preconditions:
        1 <= len(bills) <= 10^5
        bills[i] is either 5, 10, or 20

    Examples:
        >>> solution_one([5, 5])
        True
        >>> solution_one([5, 5, 10])
        True
        >>> solution_one([10, 20, 5, 5, 5])
        False
    """
    five = ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


if __name__ == '__main__':
    doctest.testmod()
