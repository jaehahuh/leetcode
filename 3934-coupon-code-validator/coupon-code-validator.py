import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]: 
        def check_code(s):
            if not s:
                False
            return re.fullmatch(r'[a-zA-Z0-9_]+', s) is not None 

        n = len(code)
        busin_categories = ("electronics", "grocery", "pharmacy", "restaurant")
        valid_coupons = []
        for i in range(n):
            if not check_code(code[i]):
                continue
            if not businessLine[i] in busin_categories:
                continue
            if not isActive[i]:
                continue
            valid_coupons.append((businessLine[i], code[i]))
        valid_coupons.sort()
        return [c for b, c in valid_coupons]