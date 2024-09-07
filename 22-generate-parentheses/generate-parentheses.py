class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(curr, left, right):
            if len(curr) == 2*n:
                res.append(curr)
                return
    
            if left < n:
                backtracking(curr + "(", left + 1, right)
            
            if right < left:
                backtracking(curr + ")", left, right+1)
    

        backtracking("", 0, 0)
        return res