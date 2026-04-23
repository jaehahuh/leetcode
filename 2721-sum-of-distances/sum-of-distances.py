class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        n = len(nums)
        result = [0] * n

        for index in indices:
            group = indices[index]
            total_sum = sum(group)
            count = len(group)

            left_sum = 0
            for i, current_idx in enumerate(group):
                right_sum = total_sum - left_sum - current_idx
                left_part = i * current_idx - left_sum
                right_part = right_sum - (count - i - 1) * current_idx
                result[current_idx] = left_part + right_part
                left_sum += current_idx
        return result