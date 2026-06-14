# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 중간 노드 찾기 (slow, fast 포인터)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 뒷부분 리스트 뒤집기
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 앞부분(head)과 뒤집힌 리스트(prev)를 순회하며 쌍대 합 구하기
        max_sum = 0
        front = head
        back = prev
        while back:
            max_sum = max(max_sum, front.val + back.val)
            front = front.next
            back = back.next
        
        return max_sum