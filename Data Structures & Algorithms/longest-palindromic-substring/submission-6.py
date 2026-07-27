class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        ans = ''
        maxLen = 0
        for length in range(1,n+1):
            for start in range(n-length+1):
                end = start+length-1
                if length == 1:
                    dp[start][end] = True
                elif length == 2:
                    dp[start][end] = (s[start] == s[end])
                else :
                    dp[start][end] = (s[start]==s[end] and dp[start+1][end-1])
                if dp[start][end] and length>maxLen:
                    ans = s[start:end+1]
                    maxLen = length
        return ans

                