class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # define optimal value of i
        # OPT[i] = minmum number of coins required to make amount i
        # OPT[i] = min(OPT[i-c]) + 1, where c are the types of coins available
        

        OPT = [amount + 1] * (amount + 1)
        
        OPT[0] = 0

        for i in range(len(OPT)):
            for c in coins:
                if i - c >= 0:
                    OPT[i] = min(OPT[i], 1+OPT[i-c])

        return -1 if OPT[len(OPT)-1] == amount+1 else OPT[len(OPT)-1]