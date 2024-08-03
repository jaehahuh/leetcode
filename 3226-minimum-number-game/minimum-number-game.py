class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) != 0:
            alice = min(nums)
            nums.remove(alice)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)

        return arr