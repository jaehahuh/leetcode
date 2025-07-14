# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary_num = []
        while head:
            binary_num.append(head.val)
            head = head.next

        decimal_val = 0
        binary_num.reverse()
        for i in range(len(binary_num)):
            decimal_val += binary_num[i] * (2**i)

        return decimal_val