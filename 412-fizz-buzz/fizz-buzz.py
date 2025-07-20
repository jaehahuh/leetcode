class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rules = {3: "Fizz", 5: "Buzz"}
        result = []
        for i in range(1, n+1):
            s = ''
            for key, val in rules.items():
                if i % key == 0:
                    s += val

            if s != '':
                result.append(s)
            else:
                result.append(str(i))
        
        return result