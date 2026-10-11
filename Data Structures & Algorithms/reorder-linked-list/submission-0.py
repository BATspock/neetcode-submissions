# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6] => [0, 6, 1, 5, 2, 4, 3]
        # [0 -> 1 -> 2 -> 3 --
        # -- 4 -> 5 -> 6] => [6 -> 5 -> 4]
        # split list in two halves 
        # even = len // 2 -> both halves
        # odd = first half  = len // 2, rest if second half

        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None #this breaks in 2 halves

        prev = None
        # reverse second half
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        second = prev

        first = head
        # merge by alternating
        while second:
            tmp_first, tmp_second = first.next, second.next
            first.next = second
            second.next = tmp_first
            first, second = tmp_first, tmp_second



            


        

        
        

        