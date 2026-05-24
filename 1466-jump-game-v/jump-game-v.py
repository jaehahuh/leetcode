class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n 

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            max_reach = 1  # 자기 자신 포함 방문 1개

            # 왼쪽 점프
            for x in range(1, d+1):
                left = i - x
                if left < 0 or arr[left] >= arr[i]:
                    break  # arr[left]가 i보다 크거나 같으면 점프 불가
                max_reach = max(max_reach, 1 + dfs(left))

            # 오른쪽 점프
            for x in range(1, d+1):
                right = i + x
                if right >= n or arr[right] >= arr[i]:
                    break  # arr[right]가 i보다 크거나 같으면 점프 불가
                max_reach = max(max_reach, 1 + dfs(right))

            dp[i] = max_reach
            return dp[i]

        result = 0
        for i in range(n):
            result = max(result, dfs(i))
        return result
