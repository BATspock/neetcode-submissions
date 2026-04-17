class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = [0,0,0]
        # for num in nums:
        #     if num == 0:
        #         count[0]+=1
        #     elif num == 1:
        #         count[1]+=1
        #     else:
        #         count[2]+=1

        # print(count)

        # i = 0
        # for j in range(len(count)):
        #     while count[j]:
        #         nums[i] = j
        #         count[j]-=1
        #         i+=1

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        left, right = 0, len(nums)-1
        i = 0

        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left+=1

            elif nums[i] == 2:
                swap(i, right)
                right-=1
                i-=1 # do not directly increment i because it can introduce 0 in middle of the array
            i+=1
