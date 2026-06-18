class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp =[0]*n
        total_multi = 1
        zero_count = nums.count(0)
        if zero_count>1:
            return temp
        for i in range(n):
            if(nums[i]!=0):
                total_multi *= nums[i] 
        
        for i in range(n):
            if zero_count == 1:
                if nums[i]==0:
                    temp[i] = total_multi
            else :
                temp[i] = total_multi//nums[i]
        return temp
        