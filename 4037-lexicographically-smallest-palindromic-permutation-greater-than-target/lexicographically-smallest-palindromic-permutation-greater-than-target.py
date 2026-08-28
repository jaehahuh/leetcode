class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)

        odd_chars = [c for c, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""  
            
        mid_char = odd_chars[0] if len(odd_chars) == 1 else ""
        
        half_counts = {c: cnt // 2 for c, cnt in counts.items() if cnt // 2 > 0}
        half_len = n // 2

        max_match = 0
        curr_counts = half_counts.copy()
        for i in range(half_len):
            t_char = target[i]
            if curr_counts.get(t_char, 0) > 0:
                curr_counts[t_char] -= 1
                max_match += 1
            else:
                break
                
        if max_match == half_len:
            first_half = target[:half_len]
            full_palin = first_half + mid_char + first_half[::-1]
            if full_palin > target:
                return full_palin

        remain_counts = half_counts.copy()
        for i in range(max_match):
            remain_counts[target[i]] -= 1

        for i in range(max_match, -1, -1):
            if i < max_match:
                remain_counts[target[i]] += 1
                
            if i >= half_len:
                continue
                
            target_char = target[i]
            
            for next_code in range(ord(target_char) + 1, ord('z') + 1):
                next_ch = chr(next_code)
                if remain_counts.get(next_ch, 0) > 0:
 
                    first_half_list = []
         
                    first_half_list.append(target[:i])
      
                    first_half_list.append(next_ch)
                    remain_counts[next_ch] -= 1
                    

                    for code in range(ord('a'), ord('z') + 1):
                        ch = chr(code)
                        if remain_counts.get(ch, 0) > 0:
                            first_half_list.append(ch * remain_counts[ch])
                            
                    first_half = "".join(first_half_list)

                    return first_half + mid_char + first_half[::-1]
                    
        return ""