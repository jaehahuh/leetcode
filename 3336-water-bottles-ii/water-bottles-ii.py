class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drink = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            total_drink += 1
            empty_bottles += 1
            numExchange += 1
        
        return total_drink