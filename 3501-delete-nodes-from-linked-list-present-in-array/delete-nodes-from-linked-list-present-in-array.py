# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        #convert the nums list into a set(hash map) for faster lookups
        set_nums = set(nums)

        #make dummy_node
        node = ListNode()
        node.next = head

        prev, curr = node, head

        #move linked list
        while curr:
            if curr.val in set_nums:
                prev.next = curr.next
            else:
                prev = curr #move prev to curr only if curr node is not removed
            curr = curr.next

        return node.next