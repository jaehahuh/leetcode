class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = 0
        skill.sort()
        check_sum = skill[0] + skill[-1]
    
        for i in range(len(skill)//2):
            low = skill[i]
            high = skill[-i - 1]
            if low + high != check_sum:
                return -1
            total += low * high

        return total