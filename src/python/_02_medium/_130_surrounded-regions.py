import doctest
from typing import List


# ---------------------------------------------------------------------
# Approach 1: DFS. Time and Space: (n), where n == m * n            ***
# ---------------------------------------------------------------------
class Solution:
    def surroundRegions(self, board: List[List[str]]) -> List[List[str]]:
        """Given an m x n matrix board containing letters 'X' and 'O',
        capture regions that are surrounded. The region is surrounded
        with 'X' cells if you can connect the region with 'X' cells and
        none of the region cells are on the edge of the board.

        Examples:
            >>> s.surroundRegions([\
            ['X', 'X', 'X'],\
            ['X', 'O', 'X'],\
            ['X', 'O', 'X'],\
            ['X', 'X', 'O']\
            ])
            [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'O']]
            >>> s.surroundRegions([['X']])
            [['X']]
        """
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][cols - 1] == 'O':
                self.dfs(board, i, cols - 1)
        for j in range(1, cols - 1):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[rows - 1][j] == 'O':
                self.dfs(board, rows - 1, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'M':
                    board[r][c] = 'O'

        return board

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or \
                grid[i][j] != 'O':
            return
        grid[i][j] = 'M'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


if __name__ == '__main__':
    doctest.testmod(extraglobs={'s': Solution()})
