class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit_count = Counter(answers)
        result = 0

        for i, num in rabbit_count.items():
            group_size = i + 1
            groups = math.ceil(num/group_size)
            result += groups * group_size

        return result 