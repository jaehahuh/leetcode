class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        
        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append("(")
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(')')
                
        return ''.join(result)