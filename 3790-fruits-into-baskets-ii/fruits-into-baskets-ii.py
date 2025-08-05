class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        baskets_used = [False] * n 

        count_placed_fruits = 0
        for fruit in fruits:
            for j in range(n):
                if not baskets_used[j] and fruit <= baskets[j]:
                    baskets_used[j] = True
                    count_placed_fruits += 1
                    break

        return len(fruits) - count_placed_fruits