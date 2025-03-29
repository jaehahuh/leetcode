class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7  # 결과를 모듈러 연산할 값
        result = 1       # 초기 점수
        
        # 1. 각 숫자의 소인수 개수(Prime Score) 계산
        prime_scores = []  # 각 숫자의 소인수 개수를 저장할 리스트
        for n in nums:
            num = n      # 원본 값을 보존하기 위해 복사
            score = 0
            # 2부터 sqrt(n)까지의 수로 소인수 판별
            for factor in range(2, int(sqrt(num)) + 1):
                if num % factor == 0:
                    score += 1  # 소인수 발견 시 점수 증가
                    # 같은 소인수가 중복으로 있는 경우 모두 나누기
                    while num % factor == 0:
                        num //= factor       
            # 남은 수가 2 이상이면 소인수가 존재함
            if num >= 2:
                score += 1
            prime_scores.append(score)
        
        # 2. 각 숫자가 후보로 선택될 수 있는 부분 배열 범위 계산
        # left_bound[i] : 왼쪽에 더 큰 prime score를 가진 숫자의 인덱스 (없으면 -1)
        # right_bound[i]: 오른쪽에 더 큰 prime score를 가진 숫자의 인덱스 (없으면 len(nums))
        n_len = len(nums)
        left_bound = [-1] * n_len
        right_bound = [n_len] * n_len

        stack = []  # 모노토닉 스택 (prime score가 감소하거나 같은 순서로 유지되는 인덱스 저장)
        for i, score in enumerate(prime_scores):
            # 현재 숫자의 prime score보다 작은 스택의 인덱스들은 오른쪽 경계 갱신
            while stack and prime_scores[stack[-1]] < score:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                # 현재 숫자의 왼쪽 경계는 스택 top에 해당하는 인덱스
                left_bound[i] = stack[-1]
            stack.append(i)
        
        # 3. 각 숫자가 선택될 수 있는 횟수를 계산하여 최대 힙(음수값 활용) 구성
        # 해당 숫자가 후보로 선택될 수 있는 부분 배열의 개수는
        # (i - left_bound[i]) * (right_bound[i] - i) 로 계산됨.
        max_heap = [(-num, i) for i, num in enumerate(nums)]
        heapify(max_heap)
        
        # 4. k번의 연산으로 최대 점수 계산
        while k > 0:
            # 최대 힙에서 가장 큰 숫자(음수이므로 부호 반전)와 인덱스 추출
            neg_num, index = heappop(max_heap)
            num = -neg_num
            
            # 해당 숫자가 후보로 선택될 수 있는 부분 배열의 개수 계산
            left_count = index - left_bound[index]
            right_count = right_bound[index] - index
            count = left_count * right_count
            
            # k와 해당 숫자가 선택 가능한 횟수 중 작은 값을 연산 횟수로 결정
            operations = min(count, k)
            result = (result * pow(num, operations, MOD)) % MOD
            k -= operations
    
        return result