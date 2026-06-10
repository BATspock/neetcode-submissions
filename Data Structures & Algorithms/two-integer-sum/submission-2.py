class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = dict()
        for i in range(len(nums)):
            index_dict[nums[i]] = i
        
        for i in range(len(nums)):
            k = target - nums[i]
            
            if k in index_dict and index_dict[k]!= i:
                return [i, index_dict[k]]