class MyCircularQueue:

    def __init__(self, k: int):
        self.maxlen = k
        self.queue = [None] * self.maxlen
        self.f = 0 #front pointer
        self.r = 0 #rear pointer
        
    def enQueue(self, value: int) -> bool:
        if self.queue[self.r] is None:
            self.queue[self.r] = value
            self.r = (self.r + 1) % self.maxlen
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.queue[self.f] is None:
            return False
        else:
            self.queue[self.f] = None
            self.f = (self.f + 1) % self.maxlen
            return True
        
    def Front(self) -> int:
        if self.queue[self.f] is None:
            return -1
        else:
            return self.queue[self.f]

    def Rear(self) -> int:
        if self.queue[self.r - 1] is None:
            return -1
        else:
            return self.queue[self.r - 1]

    def isEmpty(self) -> bool:
        return self.f == self.r and self.queue[self.f] is None

    def isFull(self) -> bool:
        return self.f == self.r and self.queue[self.f] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()