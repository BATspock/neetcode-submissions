class Solution:
    def getDistance(self, x1, y1, x2, y2) -> int:
        return abs(x1 - x2)+abs(y1 - y2)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')]* n
        visited = [False]*n
        dist[0] =0
        res = 0

        for _ in range(n):
            cur_node = -1

            for i in range(n):
                if not visited[i] and (
                    cur_node == -1 or dist[i] < dist[cur_node]
                ):
                    cur_node = i

            visited[cur_node] = True
            res += dist[cur_node]

            for i in range(n):
                if not visited[i]:
                    distance = self.getDistance(
                        points[i][0], points[i][1],
                        points[cur_node][0], points[cur_node][1]
                    )
                    dist[i] = min(dist[i], distance)
        return res