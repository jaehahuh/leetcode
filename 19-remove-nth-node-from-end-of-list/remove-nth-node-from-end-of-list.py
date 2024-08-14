# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        start = ListNode(0, head)
        p1 = p2 = start
        
        # increasing the distance difference between p1 and p2 by n
        for i in range(n+1):
            p1 = p1.next
        
        # move both pointers until p1 reaches the end
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        # skip(which is remove) n th Node from end of list
        p2.next = p2.next.next

        #return new head
        return start.next