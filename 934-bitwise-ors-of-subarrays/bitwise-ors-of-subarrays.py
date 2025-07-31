class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        all_or = set()
        current_ors_at_i_minus_one = set() 

        for num in arr:
            current_ors_at_i = {num}
        
            for prev_or_val in current_ors_at_i_minus_one:
                current_ors_at_i.add(prev_or_val | num)
            
            all_or.update(current_ors_at_i)
            current_ors_at_i_minus_one = current_ors_at_i

        return len(all_or)