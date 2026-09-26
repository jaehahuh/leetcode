class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        key = ''
        result = []
        knowledge_map = {k:v for k, v in knowledge}
        in_bracket = False

        for ch in s:
            if ch == '(':
                result.append(key)
                key = ''
            elif ch == ')':
                if key in knowledge_map:
                    result.append(knowledge_map[key])
                else:
                    result.append('?')
                key = ''
            else:
                key += ch
        result.append(key)

        return ''.join(result)