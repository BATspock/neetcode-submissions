class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        OPT = [-1]*len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if OPT[i] != -1:
                return OPT[i]

            OPT[i] = cost[i] + min(dfs(i + 1), dfs(i+2))
            return OPT[i]
        return min(dfs(0), dfs(1))