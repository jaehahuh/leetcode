class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total_money = 0
        for week in range(weeks):
            total_money += 28 + week*7
        
        for day in range(1, days+1):
            total_money += weeks + day
            
        return total_money