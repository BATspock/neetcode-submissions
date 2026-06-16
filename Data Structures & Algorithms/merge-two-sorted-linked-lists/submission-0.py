# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2 == None:
            return None

        if list1 == None or list2 == None:
            return list1 if list2 is None else list2

        # create the first empty node
        cur = ListNode()
        begin = cur

        head1 = list1
        head2 = list2

        while (head1!= None and head2!= None):
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1!=None:
            cur.next = head1
        else:
            cur.next = head2

        return begin.next

        
        # while both the lists are parsed 
        # compare list1.cur.bal and list2.cur.val
        # mark it as next of the current head