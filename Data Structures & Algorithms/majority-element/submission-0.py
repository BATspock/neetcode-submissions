class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        max = -1
        ans = 0
        for (k,v) in freq.items():
            if v > max:
                max = v
                ans = k

        return ans
