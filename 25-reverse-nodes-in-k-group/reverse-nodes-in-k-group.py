# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k) -> ListNode:
            prev,curr = None,head
            while k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        #check if there are at least k nodes left in the list
        count = 0
        node = head
        while count < k and node:
            node = node.next
            count += 1
        
        #if there are fewer than k nodes, return the head
        if count < k:
            return head
        
        #Reverse the first k nodes
        new_head = reverseLinkedList(head, k)
        
        #Recursively call on the remaining part of the list
        head.next = self.reverseKGroup(node, k)

        return new_head