class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        op1 = need1 * cost1 + need2 * cost2

        common = min(need1, need2)
        remainder1 = need1 - common
        remainder2 = need2 - common
        op2 = common * costBoth + remainder1 * cost1 + remainder2 * cost2

        max_need = max(need1, need2)
        op3 = max_need * costBoth


        return min(op1, op2, op3)