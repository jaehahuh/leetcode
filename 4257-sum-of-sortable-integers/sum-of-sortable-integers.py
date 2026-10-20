class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        divisors = []
        n = len(nums)
        result = 0
        
        # n의 모든 약수 구하기
        divisors = []
        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                divisors.append(d)
                if d != n // d:
                    divisors.append(n // d)

        for k in divisors:
            valid = True
            prev_max = float("-inf")

            for start in range(0, n, k):
                end = start + k
                segment = nums[start:end]

                # 구간의 최솟값과 최댓값
                mn = min(segment)
                mx = max(segment)

                # 원형 구간의 내림차순 지점 개수
                descents = 0

                for i in range(len(segment) - 1):
                    if segment[i] > segment[i + 1]:
                        descents += 1

                # 마지막 원소에서 첫 번째 원소로 연결
                if segment[-1] > segment[0]:
                    descents += 1

                if descents > 1:
                    valid = False
                    break

                # 인접한 구간 사이의 정렬 순서 확인
                if prev_max > mn:
                    valid = False
                    break

                prev_max = mx
            # 모든 조건을 만족하면 k를 더한다.
            if valid:
                result += k

        return result