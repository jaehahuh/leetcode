class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(s, a):
            lst = list(s)
            for i in range(1, len(lst), 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            return ''.join(lst)
        
        def rotate(s, b):
            n = len(s)
            b %= n
            return s[-b:] + s[:-b]
        
        seen = set()
        q = deque([s])
        seen.add(s)
        smallest = s
        while q:
            curr = q.popleft()
            if curr < smallest:
                smallest = curr
            op1 = add(curr, a)
            if op1 not in seen:
                seen.add(op1)
                q.append(op1)
            
            op2 = rotate(curr,b)
            if op2 not in seen:
                seen.add(op2)
                q.append(op2)
            
        return smallest