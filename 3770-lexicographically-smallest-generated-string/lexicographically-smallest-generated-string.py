class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_length = n + m - 1
        word = [None] * total_length
        is_fixed = [False] * total_length

        # Handle all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    index = i + j
                    if word[index] is not None and word[index] != str2[j]:
                        return ''
                    word[index] = str2[j]
                    is_fixed[index] = True

        # Fill remain non-fixed slots
        for i in range(total_length):
            if word[i] is None:
                word[i] = 'a' 
        
        # Handle all 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                is_match = True
                for j in range(m):
                    if word[i+j] != str2[j]:
                        is_match = False
                        break

                if is_match:
                    changed = False
                    for j in range(m-1, -1, -1):
                        index = i + j
                        if not is_fixed[index]:
                            word[index] = 'b' if str2[j] == 'a' else 'a'
                            changed = True
                            break
                    if not changed:
                        return ''
        
        for i in range(n):
            current_sub = ''.join(word[i:i+m])
            if str1[i] == 'T' and current_sub != str2:
                return ''
            if str1[i] == 'F' and current_sub == str2:
                return ''
        
        return ''.join(word)