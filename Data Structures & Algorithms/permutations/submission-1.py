class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []   
        def helper(nums,idx,ans):
            if idx == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(idx,len(nums)):
                nums[idx],nums[i] = nums[i],nums[idx]
                helper(nums,idx+1,ans)
                nums[idx],nums[i] = nums[i],nums[idx]   
        helper(nums,0,ans)
        return ans
    
