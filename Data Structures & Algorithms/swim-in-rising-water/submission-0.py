class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        pq = [(grid[0][0], 0, 0)]
        visited.add((0,0))
        
        def isValid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        max_height = grid[0][0]

        while pq:
            height, r, c = heapq.heappop(pq)
            visited.add((r,c))
            max_height = max(max_height, height)

            if r == rows - 1 and c == cols - 1:
                return max_height

            for x, y in dirs:
                nr, nc = r + x, c + y
                if (nr, nc) not in visited and isValid(nr, nc):
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))
            
        return -1
                    
