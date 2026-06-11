class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        ans = [0]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1]*nums[i+1]

        # print(prefix)
        # print(postfix)
        # for i in range(len(nums)):
        #     ans[i] = prefix[i]*postfix[i]
        
        ans = [prefix[i]*postfix[i] for i in range(len(nums))]
        return ans
       
