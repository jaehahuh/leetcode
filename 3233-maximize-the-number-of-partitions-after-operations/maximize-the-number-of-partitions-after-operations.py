from functools import cache
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(index, current_partition_mask, can_change) -> int:
            # 베이스 케이스: 문자열의 끝에 도달하면 더 이상 파티션을 만들 수 없으므로 0 반환
            if index == n:
                return 0

            # 현재 문자의 비트마스크
            char_bit = 1 << (ord(s[index]) - ord('a'))
            # 현재 파티션 마스크에 현재 문자를 추가
            mask_with_current_char = current_partition_mask | char_bit

            # 만약 현재 문자를 추가했을 때 k개 고유 문자 제한을 초과하면
            if mask_with_current_char.bit_count() > k:
                # 현재 파티션을 종료하고 새로운 파티션을 시작합니다.
                # 새 파티션은 현재 문자로 시작하며, 카운트에 +1
                res1 = 1 + dfs(index + 1, char_bit, can_change) 
            else:
                # 현재 파티션을 계속 이어갑니다.
                res1 = dfs(index + 1, mask_with_current_char, can_change)
            

            # 현재 문자를 한 번 변경하는 기회를 사용하는 경우 (can_change가 True일 때만)
            res2 = 0
            if can_change:
                # 현재 문자를 26가지 모든 가능한 문자로 변경 시도
                for changed_char_idx in range(26):
                    changed_char_bit = 1 << changed_char_idx
                    # 변경된 문자를 현재 파티션 마스크에 추가
                    mask_with_changed_char = current_partition_mask | changed_char_bit

                    # 변경된 문자를 추가했을 때 k개 고유 문자 제한을 초과하면
                    if mask_with_changed_char.bit_count() > k:
                        # 현재 파티션을 종료하고 새로운 파티션을 시작합니다.
                        # 새 파티션은 변경된 문자로 시작하며, 변경 기회는 소진 (False), 카운트에 +1
                        res2 = max(res2, 1 + dfs(index + 1, changed_char_bit, False))
                    else:
                        # 현재 파티션을 계속 이어갑니다. 변경 기회는 소진 (False)
                        res2 = max(res2, dfs(index + 1, mask_with_changed_char, False))
            
            # 두 경우(변경하지 않은 경우와 변경한 경우) 중 최대 파티션 개수를 반환
            return max(res1, res2)

        return dfs(0, 0, 1) + 1