import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #첫번째 리스트가 두번째 리스트보다 길면 두 리스트의 순서를 바꿔준다. 
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        start = 0
        end = len(nums1)

        partition = (len(nums1)+len(nums2)+1)//2
        isEven = (len(nums1)+len(nums2))%2 == 0

        while start <= end:
            nums1_idx = (start+end)//2
            nums2_idx = (partition - nums1_idx)
            
            #첫번째 리스트를 두 그룹으로 나눈 후 왼쪽 그룹에서는 최대값을 찾고 오른쪽 그룹에서는 최소값을 찾는다.
            max_left1 = nums1[nums1_idx-1] if nums1_idx != 0 else -math.inf  #왼쪽 그룹이 비었을 경우 -INF 값 
            min_right1 = nums1[nums1_idx] if nums1_idx != len(nums1) else math.inf  #오른쪽 그룹이 비어있을 경우 INF값 
            
            #두번째 리스트도 위와 같이 적용
            max_left2 = nums2[nums2_idx-1] if nums2_idx != 0 else -math.inf
            min_right2 = nums2[nums2_idx] if nums2_idx != len(nums2) else math.inf
            
            #첫번째 리스트와 두번째 리스트 안에서 왼쪽 그룹의 최대값이 오른쪽 그룹의 최소값보다 작은지 확인 
            if max_left1 <= min_right2 and max_left2 <=  min_right1:
                if isEven: # 두 리스트의 총 길이가 짝수 일 경우 중앙값 계산
                    return (max(max_left1,max_left2)+min(min_right1,min_right2))/2
                else: #홀수 일 경우
                    return max(max_left1, max_left2)

            
            #첫번째 리스트의 왼쪽 그룹의 최대값이 두번째 리스트의 오른쪽 그룹의 최소값 보다 큰 경우, 첫번째 그룹의 왼쪽 그룹의 크기를 한개 줄이고
            #오른쪽 그룹을의 크기를 한개 늘린다.
            elif max_left1 > min_right2:
                end = nums1_idx - 1

            else:
                start = nums1_idx+1