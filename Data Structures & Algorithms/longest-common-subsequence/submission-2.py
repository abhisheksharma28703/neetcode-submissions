class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1]*m for i in range(n)]
        def solve(i,j,dp):
            if i<0 or j<0:
                return 0
            if dp[i][j] != -1 :
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + solve(i-1,j-1,dp)
            else :
                dp[i][j] = max(solve(i-1,j,dp),solve(i,j-1,dp))
            return dp[i][j]
        return solve(len(text1)-1,len(text2)-1,dp)