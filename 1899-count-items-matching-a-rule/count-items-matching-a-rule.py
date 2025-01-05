class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        index_dic = {"type": 0, "color": 1, "name": 2}
        index = index_dic[ruleKey]

        for i in range(len(items)):
            if items[i][index] == ruleValue:
                count += 1
         
        return count