class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner_score = stack.pop()
                curr_score = max(2*inner_score, 1)
                stack[-1] += curr_score
        return stack[0]