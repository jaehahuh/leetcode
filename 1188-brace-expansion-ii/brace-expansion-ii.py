class Solution:
  def braceExpansionII(self, expression: str) -> list[str]:
    def parse(s: str) -> set:
        # 괄호 밖의 최상위 쉼표(,)를 기준으로 분할하여 합집합(Union) 처리
        bracket_balance = 0
        for i, c in enumerate(s):
            if c == '{':
                bracket_balance += 1
            elif c == '}':
                bracket_balance -= 1
            elif c == ',' and bracket_balance == 0:
                return parse(s[:i]) | parse(s[i + 1 :])

        # 전체가 괄호로 둘러싸여 있는 경우 괄호 제거
        if s.startswith('{') and s.endswith('}'):
            bracket_balance = 0
            is_fully_enclosed = True
            for i in range(len(s) - 1):
                if s[i] == '{':
                    bracket_balance += 1
                elif s[i] == '}':
                    bracket_balance -= 1
                if bracket_balance == 0:
                    is_fully_enclosed = False
                    break
            # 루프가 끝난 직후에 올바르게 검사하도록 들여쓰기 수정
            if is_fully_enclosed:
                return parse(s[1:-1])

        # 인접한 요소들의 곱집합(Concatenation) 처리
        current_word = set([''])
        i = 0
        while i < len(s):
            if s[i] == '{':
            # 짝이 맞는 닫는 중괄호 찾기
                bracket_balance = 0
                j = i
                while j < len(s):
                    if s[j] == '{':
                        bracket_balance += 1
                    elif s[j] == '}':
                        bracket_balance -= 1
                    if bracket_balance == 0:
                        break
                    j += 1

                # while 루프가 완전히 끝난 뒤에 닫는 괄호까지의 범위를 파싱
                sub = parse(s[i : j + 1])
                current_word = {x + y for x in current_word for y in sub}
                i = j + 1
            else:
            # 연속된 문자(알파벳) 처리
                j = i
                while j < len(s) and s[j] not in '{,}':
                    j += 1
                word = s[i:j]
                current_word = {x + word for x in current_word}
                i = j

        return current_word

    return sorted(list(parse(expression)))