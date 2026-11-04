from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.pacific_set = set()
        self.atlantic_set = set()
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        rows = len(heights)
        cols = len(heights[0])

        for i in range(rows):
            self.pacific_set.add((i, 0))
            self.atlantic_set.add((i, cols - 1))

        for j in range(cols):
            self.pacific_set.add((0, j))
            self.atlantic_set.add((rows - 1, j))

        def isValid(r, c):
            return (0 <= r < rows) and (0 <= c < cols)
        
        def canReach(i, j, coast):
            visited = set()
            queue = deque()

            queue.append((i,j))

            while queue:
                i,j = queue.popleft()
                visited.add((i,j))

                if (i, j) in coast:
                    return True
                
                for dr in dirs:
                    nr, nc = i + dr[0], j + dr[1]
                    if isValid(nr, nc) and heights[nr][nc] <= heights[i][j] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False


        res = []

        for r in range(rows):
            for c in range(cols):
                if canReach(r, c, self.atlantic_set) and canReach(r, c, self.pacific_set):
                    res.append([r,c])
        return res
