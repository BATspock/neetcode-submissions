class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find smallest element (pivot) from the queue 
        # find left bound and right bound of the pivot
        # do binary search on 0 to left bound of pivot -1, pivot to end of List

        # l, r = 0, len(nums) - 1
        # # find smallest element
        # while l <= r:
        #     mid = (l + r)//2

        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid

        # if nums[l] == target:
        #     return True

        # left_bound, right_bound = l, l
        
        # # find left bound of pivot element
        # while nums[left_bound] == nums[l]:
        #     left_bound-=1

        # while nums[right_bound] == nums[l]:
        #     right_bound+=1

        # def binary_search(start, end):
            
        #     while start <= end:
        #         mid = (start + end)//2
        #         if nums[mid] == target:
        #             return True
        #         elif nums[mid] < target:
        #             start = mid + 1
        #         else:
        #             end = mid - 1
        #     return False
        
        # if left_bound > 0:
        #     found =  binary_search(0, left_bound)
        #     if found:
        #         return True
        #     else:
        #         if right_bound < len(nums) -1:
        #             return binary_search(right_bound, len(nums)-1)
        # return False


        left, right = 0 , len(nums) -1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left+=1
                right-=1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
