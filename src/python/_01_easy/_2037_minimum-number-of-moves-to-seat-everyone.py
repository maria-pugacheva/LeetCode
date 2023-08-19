import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Sort. Time: O(n log n)                                ***
# ---------------------------------------------------------------------
def solution_one(seats: List[int], students: List[int]) -> int:
    """Return the minimum number of moves required to move each student
    in students to a seat in seats.

    Notes:
        It's allowed to increase or decrease the position of the ith
        student by 1 any number of times.

    Preconditions:
        n == len(seats) == len(students)
        1 <= n <= 100
        1 <= seats[i], students[j] <= 100

    Examples:
        >>> solution_one([3, 1, 5], [2, 7, 4])
        4
        >>> solution_one([4, 1, 5, 9], [1, 3, 2, 6])
        7
        >>> solution_one([2, 2, 6, 6], [1, 3, 2, 6])
        4
    """
    seats.sort()
    students.sort()
    cnt = 0
    for i in range(len(seats)):
        cnt += abs(seats[i] - students[i])
    return cnt


if __name__ == '__main__':
    doctest.testmod()
