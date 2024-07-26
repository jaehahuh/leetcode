class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        map = {
            '2':["a","b","c"], '3':["d","e","f"], '4':["g","h","i"], 
            '5':["j","k","l"], '6':["m","n","o"], '7':["p","q","r","s"], 
            '8':["t","u","v"], '9':["w","x","y","z"],
            }
     
        def backtracking(i, cur_ch):
            if len(cur_ch) == len(digits):
                result.append(cur_ch)
                return

            for ch in map[digits[i]]:
                backtracking(i+1 , cur_ch + ch)
        
        backtracking(0, "")
        return result