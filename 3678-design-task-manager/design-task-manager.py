class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_info = {}
        self.task_heap = []

        for userid, taskid, priority in tasks:
            self.task_info[taskid] = (userid, priority)
            heapq.heappush(self.task_heap, (-priority, -taskid, taskid))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.task_heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, old_wPriority = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.task_heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.task_heap:
            neg_priority, neg_taskid, taskid = heapq.heappop(self.task_heap)
            if taskid not in self.task_info: # Already removed from the system 
                continue
            userid, curr_priority = self.task_info[taskid]
            if -neg_priority != curr_priority: # Priority changed: this is an outdated version
                continue 
            del self.task_info[taskid]
            return userid
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()