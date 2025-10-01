class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_full_bottles = empty_bottles // numExchange
            drink += new_full_bottles
            empty_bottles = (empty_bottles % numExchange) + new_full_bottles
        return drink