class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[seq1][seq2]: seq1의 GCD와 seq2의 GCD 상태를 저장
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        dp[0][0] = 1

        for x in nums:
            next_dp = [row[:] for row in dp]
            for seq1 in range(max_val + 1):
                for seq2 in range(max_val + 1):
                    count = dp[seq1][seq2]
                    if count == 0:
                        continue
                    
                    # 1. x를 첫 번째 수열(seq1)에 추가하는 경우
                    new_seq1 = math.gcd(seq1, x)
                    next_dp[new_seq1][seq2] = (next_dp[new_seq1][seq2] + count) % MOD

                    # 2. x를 두 번째 수열(seq2)에 추가하는 경우
                    new_seq2 = math.gcd(seq2, x)
                    next_dp[seq1][new_seq2] = (next_dp[seq1][new_seq2] + count) % MOD
            
            dp = next_dp
        
        # 두 수열의 GCD가 같으면서 비어있지 않은(seq > 0) 경우만 합산
        total_pairs = 0
        for seq in range(1, max_val + 1):
            total_pairs = (total_pairs + dp[seq][seq]) % MOD
        
        return total_pairs