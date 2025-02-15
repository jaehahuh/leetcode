class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(index: int, current_sum :int, target: int, square_str:str):
            if index == len(square_str) and current_sum == target:
                return True

            # Explore all possible substrings
            for end in range(index, len(square_str)):
                substring = square_str[index:end+1] # Current substring

                # Recursive call to move to the next index
                if partition(end+1, current_sum + int(substring), target, square_str):
                    return True

            return False

        total_punishment = 0
        for i in range(1, n + 1):
            square = i * i
            square_str = str(square) 
            if partition(0, 0, i, square_str):
                total_punishment += square

        return total_punishment 