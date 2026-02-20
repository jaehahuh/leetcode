class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        result = []
        count = 0
        start = 0
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:  # ch == '0'
                count -= 1
        
            if count == 0:
                # 내부 스페셜 문자열 재귀 호출
                inner = self.makeLargestSpecial(s[start + 1:i])
                # '1' + 내부 문자열 + '0' 형태로 감싸기
                result.append('1' + inner + '0')
                start = i + 1
            
    
        # 부분 문자열들을 사전순 내림차순 정렬 후 합치기
        return ''.join(sorted(result, reverse=True))