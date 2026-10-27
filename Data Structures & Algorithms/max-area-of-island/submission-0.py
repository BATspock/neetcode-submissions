class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j, area):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return 0

            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            

            left = dfs(i , j - 1, area)
            right = dfs(i, j + 1, area)
            top = dfs(i - 1, j, area)
            bottom = dfs(i + 1, j, area)

            area = 1 + left + right + top + bottom

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c, 0))

        return max_area

