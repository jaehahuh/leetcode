class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        save_indice = []  # store temperatures list's index 
        warm_days = [0]*len(temperatures) 

        for i, temp in enumerate(temperatures):
            while save_indice and temp > temperatures[save_indice[-1]]:
                index = save_indice.pop()
                warm_days[index] = i - index 
            save_indice.append(i)
 
        return warm_days