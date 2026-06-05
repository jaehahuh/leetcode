class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculate_waviness_up_to(target_num: int) -> int:
            if target_num < 100:
                return 0
            
            target_str = str(target_num)
            total_length = len(target_str)
            
            @lru_cache(None)
            def fill_blanks(current_index: int, second_last_digit: int, last_digit: int, is_touching_limit: bool, has_started: bool):
                if current_index == total_length:
                    return (1, 0)
                
                max_digit_allowed = int(target_str[current_index]) if is_touching_limit else 9
                
                total_ways_to_finish = 0
                total_waviness_accumulated = 0
                
                for current_digit in range(max_digit_allowed + 1):
                    still_touching_limit = is_touching_limit and (current_digit == max_digit_allowed)
                    
                    if not has_started:
                        if current_digit == 0:
                            ways, wav = fill_blanks(current_index + 1, -1, -1, still_touching_limit, False)
                        else:
                            ways, wav = fill_blanks(current_index + 1, -1, current_digit, still_touching_limit, True)
                    
                    else:
                        waviness_found_here = 0
                        
                        if second_last_digit != -1 and last_digit != -1:
                            is_peak = (second_last_digit < last_digit) and (last_digit > current_digit)
                            is_valley = (second_last_digit > last_digit) and (last_digit < current_digit)
                            
                            if is_peak or is_valley:
                                waviness_found_here = 1
                        
                        ways, wav = fill_blanks(current_index + 1, last_digit, current_digit, still_touching_limit, True)
                        wav += waviness_found_here * ways
                    
                    total_ways_to_finish += ways
                    total_waviness_accumulated += wav
                    
                return (total_ways_to_finish, total_waviness_accumulated)
            
            return fill_blanks(0, -1, -1, True, False)[1]

        return calculate_waviness_up_to(num2) - calculate_waviness_up_to(num1 - 1)