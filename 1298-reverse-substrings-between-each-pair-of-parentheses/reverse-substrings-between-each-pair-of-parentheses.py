class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                curr = []
                while stack and stack[-1] != '(':
                    curr.append(stack.pop())
                
                if stack and stack[-1] == '(':
                    stack.pop()
                
                for c in curr:
                    stack.append(c)
                
            else:
                stack.append(ch)
        
        return ''.join(stack)