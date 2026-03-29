class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        visited = set()

        def dfs(current):
            if current == s2:
                return True
            if current in visited:
                return False
            visited.add(current)

            s1_lst = list(current)

            s1_lst[0], s1_lst[2] = s1_lst[2], s1_lst[0]
            if dfs("".join(s1_lst)):
                return True
            
            s1_lst[0], s1_lst[2] = s1_lst[2], s1_lst[0]
            
            s1_lst[1], s1_lst[3] = s1_lst[3], s1_lst[1]
            if dfs("".join(s1_lst)):
                return True

            s1_lst[1], s1_lst[3] = s1_lst[3], s1_lst[1]
            return False

        return dfs(s1)