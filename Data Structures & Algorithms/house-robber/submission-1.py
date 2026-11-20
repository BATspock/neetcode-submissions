class Solution:
    def rob(self, nums: List[int]) -> int:
        # OPT[i] = max(nums[i]+ nums[i - 2], nums[i - 1])
        # Optimal value at i is maximum cost from eithter robbing that house and the on before or not robbing that house but robbing the previous one
        '''
        n = len(nums)
        OPT = [-1]* n

        def dfs(i):
            if i >=n:
                return 0

            if OPT[i]!= -1:
                return OPT[i]

            OPT[i] = max(nums[i]+ dfs(i+2), dfs(i+1))

            return OPT[i]

        return dfs(0)
        '''
        if len(nums) == 1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        OPT = [0]* n

        OPT[0] = nums[0]
        OPT[1] = max(nums[0], nums[1])

        for i in range(2, n):
            OPT[i] = max(nums[i] + OPT[i-2], OPT[i-1])
        return OPT[-1]