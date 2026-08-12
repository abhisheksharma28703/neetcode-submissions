class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def solve(i,total,dp):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            add = solve(i+1,total-nums[i],dp)
            subtract = solve(i+1,total+nums[i],dp)
            dp[(i,total)] = add + subtract
            return dp[(i,total)]
        solve(0,0,dp)
        return dp[(0,0)]