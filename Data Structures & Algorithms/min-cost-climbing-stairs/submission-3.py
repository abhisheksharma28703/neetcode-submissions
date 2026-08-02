class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        def dp1(idx):
            if idx > len(cost)-1:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            dp[idx] = cost[idx]+min(dp1(idx+1),dp1(idx+2))
            return dp[idx]
        return min(dp1(0),dp1(1))
