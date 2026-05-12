class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        start_energy = 0  
        current_energy = 0 

        for actual, minimum in tasks:
            start_energy = max(start_energy, current_energy + minimum)
            current_energy += actual

        return start_energy