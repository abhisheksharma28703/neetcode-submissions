class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def func(i,nums):
            if len(nums) ==1:
                return nums[0]
            elif i == 0:
                return nums[i]*nums[i+1]
            elif i == len(nums)-1:
                return nums[i-1]*nums[i]
            return nums[i-1]*nums[i]*nums[i+1]

        def solve(nums):
            if len(nums) <= 1:
                return nums[0]
            if tuple(nums) in dp:
                return dp[tuple(nums)]
            ans = float('-inf')
            for i in range(len(nums)):
                temp = nums[:i] + nums[i+1:]
                ans = max(ans,solve(temp)+func(i,nums))
            dp[tuple(nums)] = ans
            return ans
        return solve(nums)
        

            
        