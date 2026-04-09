class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        #루트 분할 임계값 설정
        T = int(n**0.5) + 1
        
        groups = [[] for _ in range(T)]
        for l, r, k, v in queries:
            if v == 1: continue # 1을 곱하는 건 변화가 없으므로 스킵
            if k < T:
                groups[k].append((l, r, v))
            else:
                # k가 크면 직접 연산 (최대 n/T번 루프)
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % mod

        # 작은 k값들에 대한 차분 배열 처리
        dif = [1] * (n + T + 1)
        for k in range(1, T):
            if not groups[k]:
                continue
            
            # dif 배열 초기화
            for i in range(n + k + 1): dif[i] = 1
            
            for l, r, v in groups[k]:
                dif[l] = (dif[l] * v) % mod
                # k 간격 차분 배열의 끝점 계산
                last_idx = l + ((r - l) // k) * k
                end_pos = last_idx + k
                dif[end_pos] = (dif[end_pos] * pow(v, mod - 2, mod)) % mod

            # k 간격으로 누적곱 계산 (Prefix Product over step k)
            for i in range(k, n):
                dif[i] = (dif[i] * dif[i - k]) % mod
            
            # 결과 반영
            for i in range(n):
                if dif[i] != 1:
                    nums[i] = (nums[i] * dif[i]) % mod

        res = 0
        for x in nums:
            res ^= x
        return res