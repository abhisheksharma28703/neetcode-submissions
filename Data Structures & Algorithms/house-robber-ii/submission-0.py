class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def roblinear(house):
            dp = [-1]*len(house)
            def robber(idx):
                if idx>=len(house):
                    return 0
                if dp[idx]!=-1:
                    return dp[idx]
                dp[idx] = max(house[idx]+robber(idx+2),robber(idx+1))
                return dp[idx]
            return robber(0)
        return max(roblinear(nums[1:]),roblinear(nums[:-1]))

            
            