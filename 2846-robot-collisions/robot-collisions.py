class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = []
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])
        robots.sort()

        stack = []
        for i in range(n):
            curr = robots[i]
            if curr[2] == 'R':
                stack.append(curr)
            else:
                while stack and curr[1] > 0:
                    prev = stack[-1]
                    if curr[1] > prev[1]:
                        stack.pop()
                        curr[1] -= 1
                        prev[1] = 0 #removed
                    elif curr[1] < prev[1]:
                        prev[1] -= 1
                        curr[1] = 0
                        break
                    else:
                        stack.pop()
                        curr[1] = 0
                        prev[1] = 0
                        break

        robots.sort(key=lambda x: x[3])
        return [r[1] for r in robots if r[1] > 0]