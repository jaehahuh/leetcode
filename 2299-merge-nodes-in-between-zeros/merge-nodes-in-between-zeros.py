# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p.next:
            #node will keep track of the start of the next segment we are going to sum up.
            node = p.next
            p = p.next

            #sum up all nodes until we hit the next zero.
            while p.next.val != 0:
                node.val += p.next.val
                p = p.next
            
            #p is at a node with value 0, move it one step further.
            p = p.next

            # This removes the nodes with value 0 from the list.
            node.next = p.next

        return head.next