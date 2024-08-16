import doctest
from this import s


class Solution:
    @staticmethod
    def guess(num: int, pick: int) -> int:
        """If num > pick, return -1. If num < pick, return 1. Return 0
        if num == pick.
        """
        if num > pick:
            return -1
        elif num < pick:
            return 1
        return 0

    # ------------------------------------------------------------------
    # Approach 1: Check All. Time: O(n)                             ***
    # ------------------------------------------------------------------
    def solution_one(self, n: int, pick: int) -> int:
        """We are playing the Guess Game. I pick a number from 1 to n.
        You have to guess which number I picked. Return the number that
        I picked by utilizing the guess API.

        Examples:
            >>> s.solution_one(10, 6)
            6
            >>> s.solution_one(1, 1)
            1
            >>> s.solution_one(2, 1)
            1
        """
        for x in range(1, n + 1):
            if self.guess(x, pick) == 0:
                return x

    # ------------------------------------------------------------------
    # Approach 2: Binary Search. Time: O(log n)                     ***
    # ------------------------------------------------------------------
    def solution_two(self, n: int, pick: int) -> int:
        """We are playing the Guess Game. I pick a number from 1 to n.
        You have to guess which number I picked. Return the number that
        I picked by utilizing the guess API.

        Examples:
            >>> s.solution_two(10, 6)
            6
            >>> s.solution_two(1, 1)
            1
            >>> s.solution_two(2, 1)
            1
        """
        i, j = 1, n
        while i <= j:
            mid = (i + j) // 2
            res = self.guess(mid, pick)
            if res < 0:
                j = mid - 1
            elif res > 0:
                i = mid + 1
            else:
                return mid


if __name__ == '__main__':
    doctest.testmod(extraglobs={'s': Solution()})
