class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        swap_need = 0

        for ch in s:
            if ch == "[":
                balance += 1
            else:
                balance -= 1

            # If balance is negative, it has an excess closing bracket
            if balance < 0:
                swap_need += 1 # We need a swap to fix this excess
                balance += 2 # Simulate the swap by adjusting the balance
        
        return swap_need