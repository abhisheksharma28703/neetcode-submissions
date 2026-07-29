class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(idx,total_tillnow,subset):
            if total_tillnow==target:
                res.append(subset.copy())
                return
            if idx>=len(nums) or total_tillnow>target:
                return
            subset.append(nums[idx])
            backtrack(idx,total_tillnow+nums[idx],subset)
            subset.pop()
            backtrack(idx+1,total_tillnow,subset)

                
            
        backtrack(0,0,subset)
        return res
            