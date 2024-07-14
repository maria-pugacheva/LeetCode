import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: Depth First Search. Time: O(m * n)                    !**
# ---------------------------------------------------------------------
class Solution:

    def countIslands(self, grid: List[List[str]]) -> int:
        """Given an m x n 2D binary grid grid which represents a map of
        '1's (land) and '0's (water), return the number of islands.

        Examples:
            >>> s.countIslands([\
            ["1","1","1","1","0"],\
            ["1","1","0","1","0"],\
            ["1","1","0","0","0"],\
            ["0","0","0","0","0"]\
            ])
            1
            >>> s.countIslands([\
            ["1","1","0","0","0"],\
            ["1","1","0","0","0"],\
            ["0","0","1","0","0"],\
            ["0","0","0","1","1"]\
            ])
            3
        """
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return
        grid[i][j] = '*'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


if __name__ == '__main__':
    doctest.testmod(extraglobs={'s': Solution()})
