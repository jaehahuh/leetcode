class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_num_divisors(n):
            if n == 1:
                return (1, 1)
            total_count = 1
            total_sum_of_divisors = 1

            number = n
        
            exp2 = 0
            while number % 2 == 0:
                exp2 += 1
                number //= 2

            if exp2 > 0:
                total_count *= (exp2 + 1)
                total_sum_of_divisors *= (2 **(exp2 + 1) - 1)

            curr_prime = 3
            while curr_prime * curr_prime <= number:
                exp_curr_prime = 0

                while number % curr_prime == 0:
                    exp_curr_prime += 1
                    number //= curr_prime
                
                if exp_curr_prime > 0:
                    total_count *= (exp_curr_prime + 1)
                    sum_component_for_prime = (curr_prime**(exp_curr_prime + 1) 
                    - 1) // (curr_prime - 1)
                    total_sum_of_divisors *= sum_component_for_prime
                
                curr_prime += 2
        
            if number > 1:
                total_count *= (1 + 1)
                total_sum_of_divisors *= (number + 1)
            
            return (total_count, total_sum_of_divisors)
        
        result = 0
        for num in nums:
            count, total_sum = get_num_divisors(num)
            if count == 4:
                result += total_sum
        
        return result