# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #count linked list
        counter = ListNode()
        counter.next = head
        count = 0
        while counter.next:
            counter = counter.next
            count += 1
        
        #calculate the size of each part
        quotient = count // k
        remainder = count % k

       
        res = []
        curr = head
        #split the list into k parts
        for i in range(k):
            part_head = curr
            if i < remainder:
                part_leng = quotient + 1
                
            else:
                part_leng = quotient
                

            for j in range(part_leng - 1):
                if curr:
                    curr = curr.next

            # break the current part from the rest of the list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            #add the current part to the result
            res.append(part_head)
        
        return res