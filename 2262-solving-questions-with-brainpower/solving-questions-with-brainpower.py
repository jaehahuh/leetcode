class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)

        # Traverse the questions in reverse order
        for i in range(len(questions)-1, -1, -1):
            point, brain = questions[i]

            #Solve the question
            if i + brain + 1 <= len(questions):
                solve = point + dp[i + brain + 1]
            else:
                solve = point

            #Skip the question
            skip = dp[i + 1]

            # Store the maximum points between solving and skipping the current question
            dp[i] = max(solve, skip)
        return dp[0]