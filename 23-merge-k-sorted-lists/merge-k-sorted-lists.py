class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                if (i+1) < len(lists):
                    lst2 = lists[i+1] 
                else:
                    lst2 = None
                mergedLists.append(self.mergeList(lst1,lst2)) 
            lists = mergedLists

        return lists[0] # return head of lists

    #Merge Two list Node
    def mergeList(self,lst1:ListNode,lst2:ListNode) -> ListNode:
        tmp = ListNode()
        tail = tmp

        while lst1 and lst2:
            if lst1.val  < lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next
        if lst1:
            tail.next = lst1
        if lst2:
            tail.next = lst2
        return tmp.next