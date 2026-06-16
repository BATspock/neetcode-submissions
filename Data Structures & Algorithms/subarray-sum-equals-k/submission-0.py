class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = curSum = 0

        prefix_sums = {0:1}
        for num in nums:
            curSum+=num
            diff = curSum - k
            res += prefix_sums.get(diff,0)

            prefix_sums[curSum] = 1 + prefix_sums.get(curSum, 0)

        return res
