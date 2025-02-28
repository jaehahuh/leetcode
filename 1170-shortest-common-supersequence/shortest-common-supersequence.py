class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        
        # Initialize with all prefixes of str2
        prev = [str2[j:] for j in range(m)]  
        prev.append('')  # Add an empty string at the end

        # Traverse str1 in reverse
        for i in reversed(range(n)):
            curr = [''] * m  # Array to store results for the current step
            curr.append(str1[i:])  # Add the prefix starting with the current character
            
            # Traverse str2 in reverse
            for j in reversed(range(m)):
                if str1[i] == str2[j]:
                    # If the characters are the same, take from the diagonal
                    curr[j] = str1[i] + prev[j + 1]
                else:
                    # If the characters are different, compare two options
                    option1 = str1[i] + prev[j]  # Add str1 character
                    option2 = str2[j] + curr[j + 1]  # Add str2 character
                    
                    # Choose the shorter result
                    if len(option1) <= len(option2):
                        curr[j] = option1
                    else:
                        curr[j] = option2
            
            # Update prev with the current result for the next step
            prev = curr
        
        return curr[0]
