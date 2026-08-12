class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumMax = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sumMax = max(sum,sumMax)
            if sum<0:
                sum = 0
        return sumMax
