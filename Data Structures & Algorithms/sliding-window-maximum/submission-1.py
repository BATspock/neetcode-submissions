class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # import heapq
        # heap = []
        # res = []
        
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-1*nums[i], i))

        #     if i >= k -1:
        #         while heap[0][1] <= i - k:
        #             heapq.heappop(heap)
        #         res.append(-1*heap[0][0])
        # return res

        from collections import deque
        q = deque()
        l, r = 0, 0
        ans = []

        while r < len(nums):
            # check queue and maintain monoticially decreasing queue so left is highest always
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            # on queue lenght equals k and hence forth
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l+=1
            r+=1
        return ans

