class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        key = ''
        result = []
        knowledge_map = {k:v for k, v in knowledge}
        in_bracket = False

        for ch in s:
            if ch == '(':
                in_bracket = True
                key = ''
            elif ch == ')':
                in_bracket = False
                if key in knowledge_map:
                    result.append(knowledge_map[key])
                else:
                    result.append('?')
                key = ''
            else:
                if in_bracket:
                    key += ch
                else:
                    result.append(ch)

        return ''.join(result)