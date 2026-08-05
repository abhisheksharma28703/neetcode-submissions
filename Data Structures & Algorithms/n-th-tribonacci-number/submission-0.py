class Solution:
    def tribonacci(self, n: int) -> int:
        # def solve(idx):
        #     if idx == 0 :
        #         return 0
        #     if idx == 1 or idx == 2:
        #         return 1
        #     else :
        #         return solve(idx-1) + solve(idx-2) + solve(idx-3)
        # return solve(n)
        dp = [-1]*(n+3)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            if dp[i]!=-1:
                return dp[i]
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]

        