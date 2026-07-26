class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        def dps(idx,dp):
            if idx>=len(nums):
                return 0
            if dp[idx]!=-1:
                return dp[idx]
            dp[idx] = max(nums[idx]+dps(idx+2,dp),dps(idx+1,dp))
            return dp[idx]
        return dps(0,dp)
## dp[i] tells that how much money can be robbed from starting from the ith index
       

        

        

           

