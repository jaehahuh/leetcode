class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        conv_lst = []
        for s in timePoints:
            s = s.split(":")
            hour = int(s[0])*60
            minute = int(s[1])
            conv_lst.append(hour + minute)
        
        conv_lst.sort()

        min_diff = 1440 #maximum possible difference in a day (24 * 60)

        for i in range(1, len(conv_lst)):
           min_diff = min(min_diff, conv_lst[i] - conv_lst[i - 1])
        
        #handle the circular difference (from last to first time point)
        min_diff = min(min_diff, 1440 - (conv_lst[-1] - conv_lst[0]))

        return min_diff