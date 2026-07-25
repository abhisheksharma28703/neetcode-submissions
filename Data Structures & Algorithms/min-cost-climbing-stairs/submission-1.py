class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)

        def dp1(i):
            if i>=len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(dp1(i+1),dp1(i+2))
            return dp[i]
        return min(dp1(0),dp1(1))