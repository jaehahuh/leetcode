class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def dfs(path, left, right):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return
        
            if left < n:
                path.append('(')
                dfs(path, left + 1, right)
                path.pop()

            if right < left:
                path.append(')')
                dfs(path, left, right + 1)
                path.pop()
        
        dfs([], 0, 0)
        return result