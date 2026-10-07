class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        if not s:
            return [""]
        
        q = deque([s])
        result = []
        visited = {s}
        found = False

        while q:
            curr = q.popleft()
            if isValid(curr):
                result.append(curr)
                found = True
            
            if found:
                continue
            
            for i in range(len(curr)):
                if curr[i] not in ('(',')'):
                    continue
                
                next_s = curr[:i] + curr[i+1:]
                if next_s not in visited:
                    visited.add(next_s)
                    q.append(next_s)
            
        return result