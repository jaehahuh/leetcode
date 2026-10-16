from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # 40비트를 기준으로 상위는 개수(Count), 하위는 인덱스 합(Sum)을 동시에 관리
        SHIFT = 40
        MASK = (1 << SHIFT) - 1
        bit = [0] * (n + 2)
        
        def add(pos, val_pack):
            pos += 1
            while pos <= n + 1:
                bit[pos] += val_pack
                pos += pos & -pos
                
        def query(pos):
            pos += 1
            if pos > n + 1:
                pos = n + 1
            res = 0
            while pos > 0:
                res += bit[pos]
                pos -= pos & -pos
            return res

        last = {}
        totC = 0  # 전체 요소 개수
        totS = 0  # 전체 위치 합
        g = 0     # 현재 끝점에서의 제곱 합
        ans = 0
        
        for j, v in enumerate(nums):
            p = last.get(v, -1)
            
            if p < 0:
                R = totS + totC
            else:
                q_val = query(p)
                cSuf = totC - (q_val >> SHIFT)
                sSuf = totS - (q_val & MASK)
                R = sSuf - p * cSuf
            
            # (d + 1)^2 - d^2 = 2d + 1 성질을 이용한 갱신 (누락된 곱셈 연산자 수정)
            g = (g + 2 * R + (j - p)) % MOD
            ans = (ans + g) % MOD
            
            if p >= 0:
                add(p, -((1 << SHIFT) + p))
                totC -= 1
                totS -= p
                
            add(j, (1 << SHIFT) + j)
            totC += 1
            totS += j
            
            last[v] = j
            
        return ans