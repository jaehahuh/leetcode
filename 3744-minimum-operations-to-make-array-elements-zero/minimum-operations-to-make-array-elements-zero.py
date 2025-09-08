class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        total_operation = 0

        # 빠른 계산을 위한 4의 거듭제곱 경계 (4^k), r<=1e9를 덮도록 1e9를 초과하는 값까지 포함
        # 예: [1, 4, 16, ..., 4^15=1_073_741_824]
        pow4_bounds = [1]
        while pow4_bounds[-1] <= 10**9:
            pow4_bounds.append(pow4_bounds[-1] * 4)

        # 완전 블록 누적합: k번째 블록(값이 k인 구간)의 합을 누적
        full_block_prefix = [0] * len(pow4_bounds)
        for k in range(1, len(pow4_bounds)):
            count_in_block = 3 * pow4_bounds[k - 1]  # [4^(k-1), 4^k-1] 크기
            full_block_prefix[k] = full_block_prefix[k - 1] + k * count_in_block
        
        def steps_needed(x):
            # pow4_bounds[k-1] <= x < pow4_bounds[k] -> steps = k
            return bisect.bisect_right(pow4_bounds, x)
        
        def prefix_steps(n):
            if n <= 0:
                return 0
            k = steps_needed(n) # n이 속한 단계
            total = full_block_prefix[k - 1] # 완전 블록 합
            total += k * (n - pow4_bounds[k - 1] + 1) # 마지막 부분 블록
            return total
        
        def min_operations_on_range(l, r):
            total_steps = prefix_steps(r) - prefix_steps(l - 1)
            return (total_steps + 1) // 2  # ceil(total_steps / 2)
        
        for l, r in queries:
            total_operation += min_operations_on_range(l, r)
        
        return total_operation