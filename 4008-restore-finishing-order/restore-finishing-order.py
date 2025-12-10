class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        friends_set = set(friends)
        for num in order:
            if num in friends_set:
                result.append(num)
        return result