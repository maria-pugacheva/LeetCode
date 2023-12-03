from typing import List


# ---------------------------------------------------------------------
# Approach 1: Depth First Search. Time: O(m * n)                    !**
# ---------------------------------------------------------------------
def solution_one(grid: List[List[str]]) -> int:
    """Given an m x n 2D binary grid grid which represents a map of '1's
    (land) and '0's (water), return the number of islands.
       """
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                cnt += 1
    return cnt


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or \
            grid[i][j] != '1':
        return
    grid[i][j] = '*'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
