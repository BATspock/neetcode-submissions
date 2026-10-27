class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):

            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 

            if grid[i][j] == '0' or grid[i][j] == '*':
                return 
            
            grid[i][j] = '*'

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count+=1
        return count
