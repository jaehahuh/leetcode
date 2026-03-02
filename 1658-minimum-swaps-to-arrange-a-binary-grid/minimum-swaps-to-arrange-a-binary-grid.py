class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rightmost_one = [-1] * n

        # 각 행에서 가장 오른쪽 1 위치 찾기
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    rightmost_one[i] = j
                    break
            else:
                # 1이 없으면 -1 유지
                rightmost_one[i] = -1

        swaps = 0
        for i in range(n):
            target_row = -1
            # i번째 행 기준 가장 오른쪽 1 위치가 i 이하인 행 찾기
            for j in range(i, n):
                if rightmost_one[j] <= i:
                    target_row = j
                    break

            # 못 찾으면 불가능
            if target_row == -1:
                return -1

            # target_row를 i 위치로 올림 (인접 스왑 수)
            while target_row > i:
                rightmost_one[target_row], rightmost_one[target_row-1] = rightmost_one[target_row-1], rightmost_one[target_row]
                swaps += 1
                target_row -= 1

        return swaps