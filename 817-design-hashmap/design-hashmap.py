#Seperate Chaining
class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [ListNode() for _ in range(self.size)]
    
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        cur = self.table[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        cur = self.table[index].next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        cur = self.table[index]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)