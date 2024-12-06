class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # converts the banned list to set to reduce search time, O(k), k = len(banned) 
        banned_set = set(banned)  
        current_sum = 0
        count = 0
        for num in range(1, n+1):
            if num in banned_set:
                continue
            if current_sum + num > maxSum:
                break
            current_sum += num
            count += 1
        
        return count