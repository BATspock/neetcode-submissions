class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # cheapest to dst is dijsktra
        # we need at most k stops
        # in the datastrcuture also capture how many stops are done
        # (cost, source, hops)

        # cannot process a node anymore if 
        #. - visted AND ALSO hops are more than k

        # adj = defaultdict(list)
        # visited = set()

        # for srci, dsti, costi in flights:
        #     adj[srci].append((dsti, costi))

        # pq = [(0, src, 0)]
        # res = float('inf')

        # while pq:
        #     cst, node, stops = heapq.heappop(pq)          
        #     if (node, stops) in visited:
        #         continue
        #     visited.add((node, stops))
        #     if node == dst:
        #         res = min(res, cst)
        #         continue
            
        #     for next_node, cost in adj[node]:
        #         if cost + cst < res and stops <= k:
        #             if (next_node, stops + 1) not in visited:
        #                 heapq.heappush(pq, \
        #                 (cost + cst, next_node, stops + 1))

        # return res if res!=float('inf') else -1

        prices = [float('inf')] * n
        prices[src] = 0

        adj = defaultdict(list)

        for u, v, cost in flights:
            adj[u].append([v, cost])

        q = deque([(0,src, 0)])

        while q:
            cst, node, stops = q.popleft()

            if stops > k:
                continue

            for nei, w in adj[node]:
                next_cost = cst + w
                if next_cost < prices[nei]:
                    prices[nei] = next_cost
                    q.append((next_cost, nei, stops + 1))
        return prices[dst] if prices[dst] != float('inf') else -1

