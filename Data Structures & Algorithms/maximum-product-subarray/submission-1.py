class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxPdt,minPdt = 1,1
        for num in nums:
            if num == 0:
                maxPdt,minPdt = 1,1
                continue
            temp = maxPdt*num
            maxPdt = max(maxPdt*num,minPdt*num,num)
            minPdt = min(temp,num*minPdt,num)
            res = max(res,maxPdt)
        return res
