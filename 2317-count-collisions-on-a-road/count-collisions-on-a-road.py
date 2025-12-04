class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = 0
        stack = []
        for d in directions:
            if d == 'R':
                stack.append(d)
            elif d == 'S':
                while stack and stack[-1] == 'R': # 앞에 있던 연속된 'R'들은 이 정지차와 부딪혀서 각각 +1
                    collisions += 1
                    stack.pop()
                if not stack or stack[-1] != 'S':
                    stack.append('S')
            else: # d == 'L'
                if not stack: # 앞에 아무도 없으면 왼쪽으로 가서 충돌 없음
                    continue
                if stack[-1] == 'S': # 바로 앞이 정지차이면 L이 부딪혀 +1
                    collisions += 1
                else: #stack[-1] == 'R'
                    countR = 0
                    while stack and stack[-1] == 'R':  # 연속된 모든 'R'들과 충돌
                        countR += 1
                        stack.pop()
                    collisions += countR + 1 # 연속된 R 각각이 정지(+1)하고, L 자신과 마지막 R의 첫 충돌에서 추가 +1
                    if not stack or stack[-1] != 'S':
                        stack.append('S')
            
        return collisions