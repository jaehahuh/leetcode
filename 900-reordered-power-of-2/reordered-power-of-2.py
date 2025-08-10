class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def power_of_2(x):
            return ''.join(sorted(str(x)))
        
        power_set = {power_of_2(1 << i) for i in range(30)}
        return power_of_2(n) in power_set