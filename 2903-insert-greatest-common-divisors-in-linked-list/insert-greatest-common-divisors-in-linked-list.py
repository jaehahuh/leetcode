# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            gcd_num = math.gcd(p.val, p.next.val)
            tmp = ListNode(gcd_num, p.next)
            p.next = tmp
            # move to the next pair of nodes.
            p = tmp.next        
        return head