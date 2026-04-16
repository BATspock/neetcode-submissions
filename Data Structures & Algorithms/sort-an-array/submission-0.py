class Solution:

    def merge(self, nums:List[int], left:int, middle:int, right: int)->None:
        left_arr, right_arr = nums[left: middle + 1], nums[middle+1: right+1]
        i,j,k = left, 0, 0

        while j < len(left_arr) and k < len(right_arr):
            if left_arr[j] <= right_arr[k]:
                nums[i] = left_arr[j]
                j+=1
            else:
                nums[i] = right_arr[k]
                k+=1
            i+=1

        while j < len(left_arr):
            nums[i] = left_arr[j]
            i+=1
            j+=1

        while k < len(right_arr):
            nums[i] = right_arr[k]
            i+=1
            k+=1
    
    def merge_sort(self, nums:List[int], left, right)->None:
        if left >= right:
            return 
        middle = (left + right)// 2
        self.merge_sort(nums, left, middle)
        self.merge_sort(nums, middle+1, right)
        self.merge(nums, left, middle, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums)-1)
        return nums