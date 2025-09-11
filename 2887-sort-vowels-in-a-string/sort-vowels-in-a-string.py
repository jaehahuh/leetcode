class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        order_dict = defaultdict(str)

        vowels_list = []
        for i in range(len(s)):
            if s[i] not in vowels:
                order_dict[i] = s[i]
            else:
                vowels_list.append(s[i])
        vowels_list.sort(reverse=True)

        sorted_str = []
        for i in range(len(s)):
            if i in order_dict:
                sorted_str.append(order_dict[i])
            else:
                sorted_str.append(vowels_list.pop())
        
        return ''.join(sorted_str)