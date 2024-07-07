#TOP-DOWN Memoization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #make hash map for time efficiency
        cache = {}

        #depth first search
        #i: index of s
        #j: index of p
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]


            if i >= len(s) and j >= len(p): #both indeces are out of bound then found solution.
                return True
            if j >= len(p): #p is out of bound then, there is no solution.
                return False
            
            match = i < len(s) and (s[i] == p[j] or  p[j] == ".") #check char of s,p are same
            
            #If there's * after the p[j]
            if j+1 < len(p) and p[j+1] == "*":
                cache[(i,j)] =  (dfs(i, j+2) or      # don't use * 
                        (match and dfs(i+1, j)))     # use *
                return cache[(i,j)]

            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]

            cache[(i,j)] = False
            return False
        return dfs(0,0)

''' 
examples:
1. 'a*' = ['','a','aa','a...a']
2. 'a.' = ['aa','ab','ac',...]
3. 'a..' = ['aaa','abb',..]
4. '..' = any 2 character
5. '.*' = ['','.','..']

6. 'c*a*b' = 'aab'
7. 'a*c*'= 'a'
'''