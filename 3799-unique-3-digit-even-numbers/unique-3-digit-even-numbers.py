class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        visited = [False] * n
        unique_numbers = set()

        def dfs(depth, curr_val):
            if depth == 3:
                unique_numbers.add(curr_val)
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                
                if depth == 0 and digits[i] == 0:
                    continue
                
                if depth == 2 and digits[i] % 2 != 0:
                    continue
                
                visited[i] = True
                dfs(depth + 1, curr_val * 10 + digits[i])
                visited[i] = False
            
        dfs(0,0)
        return len(unique_numbers)
