# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #get GCD between two numbers
    def gcd(num1, num2):
        for i in range(min(num1,num2),0,-1):
            if num1 % i == 0 and num2 % i == 0:
                return i

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p.next:
            gcd_num = gcd(p.val, p.next.val)
            tmp = ListNode()
            tmp.val = gcd_num
            tmp.next = p.next
            p.next = tmp
            p = tmp.next        
        return head