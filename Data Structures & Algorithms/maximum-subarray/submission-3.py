class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def solve(i,isin):
            if i == n-1:
                return max(nums[i],0) if isin else nums[i]
            if (i,isin) in dp:
                return dp[(i,isin)]
            if isin:
                temp =  max(0,solve(i+1,True)+nums[i])
            else :
                temp =  max(solve(i+1,True)+nums[i],solve(i+1,False))
            dp[(i,isin)] = temp
            return temp
        
        return solve(0,False)
