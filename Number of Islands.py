class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        count = 0
        def dfs(i, j):
            grid[i][j] = '2'
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ii, jj = (i + di, j + dj)
                if 0 <= ii < r and 0 <= jj < c and grid[ii][jj] == '1':
                    dfs(ii, jj)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count