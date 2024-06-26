class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warm_days = [] 
        answer = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while warm_days and temp > temperatures[warm_days[-1]]:
                count = warm_days.pop()
                answer[count] = i - count
            warm_days.append(i)

        return answer