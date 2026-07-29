class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        count = Counter(s[:half_len])

        mid_char = s[half_len] if n % 2 == 1 else ""
        CAP = k + 1

        def count_permutations(counts: dict, remaining_length: int) -> int:
            if remaining_length == 0:
                return 1
            
            res = 1
            curr_len = remaining_length
            
            for char_code in range(26):
                ch = chr(ord('a') + char_code)
                c = counts.get(ch, 0)
                if c > 0:   # 조합 nCr = math.comb(curr_len, c)
                    res *= math.comb(curr_len, c)
                    curr_len -= c
                    if res >= CAP:
                        return CAP
            return res

        # 전체 가능한 팰린드롬 개수 검사
        total_perms = count_permutations(count, half_len)
        if total_perms < k:
            return ""

        # 앞에서부터 한 자씩 사전순으로 확정짓기
        left_half = []
        rem_len = half_len
        
        for _ in range(half_len):
            for char_code in range(26):
                ch = chr(ord('a') + char_code)
                if count.get(ch, 0) > 0:
                    # ch를 선택했을 때 가능한 순열의 수
                    count[ch] -= 1
                    possible = count_permutations(count, rem_len - 1)
                    
                    if possible >= k:
                        # k번째 순열이 이 범위 안에 존재함 -> ch 확정
                        left_half.append(ch)
                        rem_len -= 1
                        break
                    else:
                        # 이 문자로 시작하는 팰린드롬 건너뛰기
                        k -= possible
                        count[ch] += 1  #
                        
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]