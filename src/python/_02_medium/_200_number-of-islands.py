import doctest
from typing import List
import copy


# ---------------------------------------------------------------------
# Approach 1: DFS. Time: O(m * n). Space: O(m * n) in worst case    !**
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
        gridCopy = copy.deepcopy(grid)
        for row in range(len(gridCopy)):
            for col in range(len(gridCopy[0])):
                if gridCopy[row][col] == '1':
                    self.markIslands(gridCopy, row, col)
                    cnt += 1
        return cnt

    def markIslands(self, g: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or i == len(g) or j == len(g[0]) or g[i][j] != '1':
            return
        g[i][j] = 'x'
        self.markIslands(g, i + 1, j)
        self.markIslands(g, i - 1, j)
        self.markIslands(g, i, j + 1)
        self.markIslands(g, i, j - 1)


if __name__ == '__main__':
    doctest.testmod(extraglobs={'s': Solution()})
