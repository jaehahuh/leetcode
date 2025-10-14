class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        inc = [1] * n # inc[i]: 인덱스 i에서 끝나는 '엄격히 증가하는 연속 길이'
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                inc[i] = inc[i-1] + 1
        
        # 시작점 a와 a+k에서 각각 길이 k의 증가 구간이 있는지 확인
        # 첫 구간 끝: a+k-1, 두 번째 구간 끝: a+2k-1
        for a in range(0, n-2 * k + 1):
            if inc[a + k - 1] >= k and inc[a+ 2*k - 1] >= k:
                return True
        return False