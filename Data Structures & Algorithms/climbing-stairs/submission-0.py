class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        OPT = [0]*(n+1)

        OPT[1] = 1
        OPT[2] = 2

        for i in range(3, n + 1):
            OPT[i] = OPT[i-1]+OPT[i-2]

        return OPT[n]