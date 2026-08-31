# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        if not curr or not curr.next:
            return [-1, -1]
        
        first_index = -1
        prev_index = -1
        min_distance = float('inf')
        index = 1

        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if first_index == -1:
                    first_index = index
                else:
                    min_distance = min(min_distance, index - prev_index)
                
                prev_index = index
        
            prev = curr
            curr = curr.next
            index += 1
        
        if first_index == prev_index or first_index == -1:
            return [-1, -1]
        
        max_distance = prev_index - first_index
        return [min_distance, max_distance]