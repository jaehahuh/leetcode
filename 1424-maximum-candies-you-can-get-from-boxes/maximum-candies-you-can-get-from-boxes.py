class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        visited = [False] * len(status)
        hasKey = set()
        boxes = set(initialBoxes)
        q = deque()

        #Get opened boxes
        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
                visited[box] = True

        total_candies = 0

        while q:
            box = q.popleft()
            total_candies += candies[box]

            #Get keys
            for key in keys[box]:
                if key not in hasKey:
                    hasKey.add(key)
                    if key in boxes and not visited[key] and status[key] == 0:
                        status[key] = 1
                        q.append(key)
                        visited[key] = True

            #Get new boxes
            for box in containedBoxes[box]:
                boxes.add(box)
                if status[box] == 1 and not visited[box]:
                    q.append(box)
                    visited[box] = True
                
                elif box in hasKey and not visited[box]:
                    status[box] = 1
                    q.append(box)
                    visited[box] = True

        return total_candies