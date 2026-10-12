# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from itertools import count
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create a heap and add pointer headers in the heap
        heap = []
        heapq.heapify(heap)
        counter = count()

        for lst in lists:
            if lst is not None:
                heapq.heappush(heap, (lst.val,next(counter), lst))
        
        res = ListNode(0)
        cur = res

        while heap:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, next(counter),  node.next))
        
        return res.next

