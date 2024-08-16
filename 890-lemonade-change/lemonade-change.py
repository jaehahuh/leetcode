class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollars = 0
        ten_dollars = 0

        for dollar in bills:
            if dollar == 5:
                five_dollars += 1
            
            elif dollar == 10:
                if five_dollars > 0:
                    five_dollars -= 1
                    ten_dollars += 1
                else:
                    return False

            else:
                if five_dollars > 0 and ten_dollars > 0:
                    five_dollars -= 1
                    ten_dollars -= 1
                
                elif five_dollars >= 3:
                    five_dollars -= 3

                else:
                    return False
        
        return True    