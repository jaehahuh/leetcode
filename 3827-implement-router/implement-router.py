from bisect import bisect_left, bisect_right
class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.duplicate = set()
        self.time_list = {}


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        new_packet = (source, destination, timestamp)
        if new_packet in self.duplicate:
            return False

        self.q.append(new_packet)
        self.duplicate.add(new_packet)
        lst = self.time_list.setdefault(destination, [])
        if not lst or timestamp >= lst[-1]:
            lst.append(timestamp)
        else:
            index = bisect_right(lst, timestamp)
            lst.insert(index, timestamp)
        
        # Exceed memory limit
        if len(self.q) > self.limit:
            s0, d0, t0 = self.q.popleft()
            self.duplicate.discard((s0, d0, t0))
            lst0 = self.time_list.get(d0, [])
            index0 = bisect_left(lst0, t0)
            if index0 < len(lst0) and lst0[index0] == t0:
                lst0.pop(index0)
            if not lst0:
                self.time_list.pop(d0, None) 
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.duplicate.discard((s, d, t))

        lst = self.time_list.get(d, [])
        i = bisect_left(lst, t)
        if i < len(lst) and lst[i] == t:
            lst.pop(i)
        if not lst:
            self.time_list.pop(d, None)

        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.time_list.get(destination)
        if not lst:
            return 0
        left = bisect_left(lst, startTime)
        right = bisect_right(lst, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)