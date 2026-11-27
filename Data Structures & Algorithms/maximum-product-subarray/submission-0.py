class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        cur_max , cur_min = 1, 1

        for num in nums:
            tmp = cur_max * num
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, tmp, cur_min * num)
            res = max(cur_max, res)

        return res


