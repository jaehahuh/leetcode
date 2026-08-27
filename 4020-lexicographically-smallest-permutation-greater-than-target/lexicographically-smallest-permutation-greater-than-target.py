class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count_s = Counter(s)

        # target과 앞에서부터 똑같이 맞출 수 있는 최대 길이를 구하기
        max_len = 0
        curr_counts = count_s.copy()
        for t in target:
            if curr_counts[t] > 0:
                curr_counts[t] -= 1
                max_len += 1
            else:
                break
        
        # match_len 시점까지 사용하고 남은 문자 상태 만들기
        remain_counts = count_s.copy()
        for i in range(max_len):
            remain_counts[target[i]] -= 1
        

        # 뒤에서부터 거꾸로 오며 target[i]보다 큰 문자를 넣을 위치 찾기
        for i in range(max_len, -1, -1):
            if i < max_len:
                remain_counts[target[i]] += 1
            
            if i >= n:
                continue
            
            target_char = target[i]

            # target[i]보다 알파벳 순으로 뒤에 있는 문자가 남아있는지 확인
            for next_code in range(ord(target_char) + 1, ord('z') + 1):
                next_ch = chr(next_code)

                if remain_counts[next_ch] > 0:
                    result = []
                    result.append(target[:i])
                    result.append(next_ch)
                    remain_counts[next_ch] -= 1

                    for code in range(ord('a'), ord('z') + 1):
                        ch = chr(code)
                        if remain_counts[ch] > 0:
                            result.append(ch * remain_counts[ch])
                    
                    return ''.join(result)
            
        return ''