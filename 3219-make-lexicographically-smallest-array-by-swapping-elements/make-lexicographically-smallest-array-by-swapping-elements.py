class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        num_to_group = {}

        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num] = len(groups)-1

        result = []
        for n in nums:
            i = num_to_group[n]
            result.append(groups[i].popleft())

        return result