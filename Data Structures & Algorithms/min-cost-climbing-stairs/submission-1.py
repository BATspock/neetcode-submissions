class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        OPT = [-1]*len(cost)
        # OPT is optimal cost to reach end after starting at i
        # OPT[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        '''
        def dfs(i):
            if i >= len(cost):
                return 0

            if OPT[i] != -1:
                return OPT[i]

            OPT[i] = cost[i] + min(dfs(i + 1), dfs(i+2))
            return OPT[i]
        return min(dfs(0), dfs(1))
        '''

        n = len(cost)
        OPT = [0] * (n + 1)

        for i in range(2, n + 1):
            OPT[i] = min(OPT[i - 1]+ cost[i-1], \
            OPT[i-2] + cost[i-2])
        return OPT[n]