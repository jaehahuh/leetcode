class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_dict = defaultdict(list) # Dictionary to hold lists of numbers with the same digit sum
        for i, num in enumerate(nums):
            sum_digits = sum(int(digit) for digit in str(num))
            # Append the number to the list corresponding to its digit sum
            digit_sum_dict[sum_digits].append(num) 

        # Initialize max_sum to -1, which will hold the maximum sum found
        max_sum = -1

        # Calculate the maximum sum of the two largest numbers with the same digit sum
        for num_list in  digit_sum_dict.values():
            if len(num_list) > 1:
                num_list.sort(reverse=True) 
                max_sum = max(max_sum, num_list[0] + num_list[1]) # Sum the two largest values

        return max_sum