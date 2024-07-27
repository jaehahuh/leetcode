class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [None for _ in range(len(nums))]
        def permutations_generator(chosen, used):
            
            if len(chosen) == len(nums): 
                result.append(chosen[:]) # Append a copy of chosen to result
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    chosen.append(nums[i])
                    used[i] = True
                    permutations_generator(chosen, used)
                    used[i] = None
                    chosen.pop()
                    
        permutations_generator([],used)

        return result