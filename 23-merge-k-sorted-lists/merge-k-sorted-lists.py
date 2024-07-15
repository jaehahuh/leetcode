# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoList(lst1,lst2)) 

            lists = mergedLists
        return lists[0] # return head of lists

    #Merge Two list Node in ascending order
    def mergeTwoList(self,lst1:ListNode,lst2:ListNode) -> ListNode:
        head = tail = ListNode()
    
        while lst1 and lst2: # loop until one of list is None
            #Sort the two lists in ascending order
            if lst1.val < lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next

        #Add the remaining non-empty remaining list together
        if lst1:
            tail.next = lst1
        if lst2:
            tail.next = lst2

        return head.next # return start of linked list