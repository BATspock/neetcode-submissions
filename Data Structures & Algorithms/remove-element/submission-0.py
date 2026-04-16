class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr, i, count = [], 0, 0
        while(i < len(nums)):
            if nums[i] != val:
                arr.append(nums[i])
            else:
                count+=1 
            i+=1
        for i in range(len(arr)):
            nums[i] = arr[i]
        nums = nums[:len(nums)-count]
        return len(nums)