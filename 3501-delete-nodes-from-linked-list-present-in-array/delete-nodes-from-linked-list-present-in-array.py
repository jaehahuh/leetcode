# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_nums = set(nums)
        node = ListNode()
        node.next = head

        prev, curr = node, head
        while curr:
            if curr.val in set_nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return node.next