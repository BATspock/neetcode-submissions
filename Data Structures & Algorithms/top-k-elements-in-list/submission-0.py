import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1

                
        arr = list()
        
        for item in freq.items():
            key, val = item
            arr.append((val, key))
        
        #fill all nums until len(ans) > k

        #if next num
        #   check if it larger than freq of the smallest in ans
        #   to check in O(1) maintain min heap of ans
        #   pop and push in the min heap
        ans = list()
        for f in arr:
            if len(ans) >= k:
                # check with top of min heap
                if f[0] > ans[0][0]:
                    heapq.heappop(ans)
                    heapq.heappush(ans, f)
            else:
                heapq.heappush(ans, f)
        
        
        return [val[1] for val in ans]