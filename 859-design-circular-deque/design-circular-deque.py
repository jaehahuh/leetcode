'''
class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.k = k
        self.len = 0
        self.head.right = self.tail
        self.tail.left = self.head

    #add new node
    def _add(self, node: ListNode, new_node: ListNode):
        tmp = node.right
        node.right = new_node
        new_node.left= node
        new_node.right = tmp
        tmp.left = new_node
        
    #delete node
    def _del(self, node: ListNode):
        tmp = node.right.right
        node.right = tmp
        tmp.left = node
 
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self._add(self.head, ListNode(value))
            return True
        

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self._add(self.tail.left, ListNode(value))
            return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            self._del(self.head)
            return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            self._del(self.tail.left.left)
            return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()