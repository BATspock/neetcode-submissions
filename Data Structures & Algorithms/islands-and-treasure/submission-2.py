from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # do a mulit source bfs
        queue = deque()
        dirs = [[0,-1], [0, 1], [1,0], [-1, 0]]
        INF = 2**31 -1 
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            
            row, col = queue.popleft()

            # dont add in the queue if already visitied of out of bound or treasuure or water

            for dr in dirs:
                nr, nc = row + dr[0], col + dr[1]

                if (nr >= 0 and nc >= 0 and nr < rows and nc < cols):
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = grid[row][col] + 1
                        queue.append((nr, nc))

            

            


        