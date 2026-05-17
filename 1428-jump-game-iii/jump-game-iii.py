class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set([start])
        n = len(arr)

        while queue:
            curr = queue.popleft()

            if arr[curr] == 0:
                return True
            
            for next_index in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    queue.append(next_index)

        return False