class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        V = [i for i in range(k)]
        
        M = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k - i, k):
                M[i][j] = 1
                
        # 두 행렬을 곱하는 함수 O(k^3)
        def mat_mul(A, B):
            res = [[0] * k for _ in range(k)]
            for i in range(k):
                for l in range(k):
                    if A[i][l]: # 0이 아닐 때만 연산하여 속도 최적화
                        for j in range(k):
                            res[i][j] = (res[i][j] + A[i][l] * B[l][j]) % MOD
            return res
            
        # 행렬의 분할 정복 거듭제곱 함수 O(k^3 * log(P))
        def mat_pow(mat, p):
            # 단위 행렬(Identity Matrix)로 초기화
            res = [[0] * k for _ in range(k)]
            for i in range(k):
                res[i][i] = 1
            
            base = mat
            while p > 0:
                if p % 2 == 1:
                    res = mat_mul(res, base)
                base = mat_mul(base, base)
                p //= 2
            return res
            
        # 행렬 M을 (n - 2)번 거듭제곱
        M_pow = mat_pow(M, n - 2)
        
        # 거듭제곱된 행렬 M_pow와 초기 벡터 V를 곱하여 최종 상태를 구함
        final_V = [0] * k
        for i in range(k):
            for j in range(k):
                final_V[i] = (final_V[i] + M_pow[i][j] * V[j]) % MOD
                
        # 상승으로 끝난 총합에 2를 곱해(하강 대칭 포함) 최종 정답 반환
        total_valid = (2 * sum(final_V)) % MOD
        
        return total_valid