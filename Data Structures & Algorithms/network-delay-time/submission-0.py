class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list) #{source: [dst, wt]}
        visited = set()

        for u, v, t in times:
            adj_list[u].append([t, v])

        pq = [(0,k)]        
        time = 0
        
        while pq:
            t, node = heapq.heappop(pq)
            if node in visited:
                continue

            visited.add(node)
            time = t

            for ti, dst in adj_list[node]:
                if dst not in visited:
                    heapq.heappush(pq,(t + ti, dst))

        return time if len(visited) == n else -1
