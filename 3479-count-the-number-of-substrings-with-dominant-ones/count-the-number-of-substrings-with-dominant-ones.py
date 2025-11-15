import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        zero_indices = [-1] + [i for i, char in enumerate(s) if char == '0'] + [n]
        
        max_k_limit = min(len(zero_indices) - 1, int(math.sqrt(n)) + 2) 
        
        for k in range(max_k_limit):
            
            for p_idx in range(len(zero_indices) - k - 1):
                
                if k == 0:
                    num_ones_in_block = zero_indices[p_idx + 1] - zero_indices[p_idx] - 1
                    ans += num_ones_in_block * (num_ones_in_block + 1) // 2
                    continue
                
                left_zero_idx = zero_indices[p_idx + 1]
                right_zero_idx = zero_indices[p_idx + k]
                
                left_ones_available = left_zero_idx - (zero_indices[p_idx] + 1)
                
                right_ones_available = (zero_indices[p_idx + k + 1] - 1) - right_zero_idx
                
                ones_inside_window = (right_zero_idx - left_zero_idx + 1) - k
                
                required_ones_for_k = k * k
                
                for l_shift in range(left_ones_available + 1):
                    current_total_ones = ones_inside_window + l_shift
                    
                    if current_total_ones >= required_ones_for_k:
                        ans += (right_ones_available + 1)
                    else:
                        ones_needed_from_right = required_ones_for_k - current_total_ones
                        
                        if ones_needed_from_right <= right_ones_available:
                            ans += (right_ones_available - ones_needed_from_right + 1)
                            
        return ans