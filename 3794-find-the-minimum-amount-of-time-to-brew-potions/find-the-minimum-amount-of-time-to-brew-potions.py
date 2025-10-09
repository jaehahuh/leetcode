class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        prev_wizard_finish = sum(skill) * mana[0]

        for j in range(1, m):
            prev_potion_done = prev_wizard_finish
            for i in range(n - 2, -1, -1):
                prev_potion_done -= skill[i+1] * mana[j-1]
                prev_wizard_finish = max(prev_potion_done, prev_wizard_finish - skill[i] * mana[j])
            prev_wizard_finish += sum(skill) * mana[j]
        
        return prev_wizard_finish