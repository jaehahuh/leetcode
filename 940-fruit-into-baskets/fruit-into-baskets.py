class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        left = 0
        fruit_counts = collections.defaultdict(int) 
        for right in range(len(fruits)):
            current_fruit = fruits[right]
            fruit_counts[current_fruit] += 1

            while len(fruit_counts) > 2:
                remove_fruit = fruits[left]
                fruit_counts[remove_fruit] -= 1

                if fruit_counts[remove_fruit] == 0:
                    del fruit_counts[remove_fruit]
                
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits