class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)== 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        choice1 = nums[1:]
        choice2 = nums[:-1]

        def helper(choice):
            rob1, rob2 = 0, 0

            for i in range(len(choice)):
                temp = max(choice[i]+rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(helper(choice1), helper(choice2))