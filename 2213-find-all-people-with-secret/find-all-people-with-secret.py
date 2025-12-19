class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return True
        return False

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dsu = DSU(n)
        dsu.union(0, firstPerson)

        meetings_by_time = defaultdict(list)
        for p1, p2, t in meetings:
            meetings_by_time[t].append((p1, p2))

        sorted_times = sorted(meetings_by_time.keys())
        for t in sorted_times:
            current_time_meetings = meetings_by_time[t]

            people_in_current_meetings = set()
            for p1, p2 in current_time_meetings:
                dsu.union(p1, p2)
                people_in_current_meetings.add(p1)
                people_in_current_meetings.add(p2)
        
            for person in people_in_current_meetings:
                if dsu.find(person) != dsu.find(0):
                    dsu.parent[person] = person 
        
        secret_holders = []
        root_of_secret_holders = dsu.find(0)
        for i in range(n):
            if dsu.find(i) == root_of_secret_holders:
                secret_holders.append(i)
                
        return secret_holders