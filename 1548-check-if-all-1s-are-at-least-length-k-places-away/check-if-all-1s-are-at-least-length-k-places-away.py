class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = -1
        for i in range(len(nums)) :
            if nums[i] == 1 and prev_one < 0:
                prev_one = i
            elif nums[i] == 1 and prev_one >= 0:
                distance = i - prev_one - 1
                prev_one = i
                if distance < k:
                    return False
        return True