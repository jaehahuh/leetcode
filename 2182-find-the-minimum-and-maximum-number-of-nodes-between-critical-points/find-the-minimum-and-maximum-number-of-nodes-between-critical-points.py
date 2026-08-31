# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []
        node = head
        index = 1
        prev = None
        while node.next:
            nxt = node.next.val
            if prev:
                if (node.val < prev and node.val < nxt) or (node.val > prev and node.val > nxt):
                    critical_points.append(index)                    
            prev = node.val
            node = node.next
            index += 1
        
        n = len(critical_points)
        if n < 2:
            return [-1,-1]
        
        max_distance = critical_points[-1] - critical_points[0]

        min_distance = float('inf')
        for i in range(1,n):
            distance = critical_points[i] - critical_points[i-1]
            if distance < min_distance:
                min_distance = distance
        
        return [min_distance, max_distance]