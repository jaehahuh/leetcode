class Solution:
    def maxFreqSum(self, s: str) -> int:
        sum_freq = 0
        vowels = 'aeiou'
        count_dict = Counter(s)
        count_list = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
        for item in count_list:
            ch, count = item
            print(ch, count)
            if ch in vowels:
                sum_freq += count
                break
                
        for item in count_list:
            ch, count = item
            if ch not in vowels:
                sum_freq += count
                break

        return sum_freq