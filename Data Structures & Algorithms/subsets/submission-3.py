class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(subsets.copy())
                return 
            subsets.append(nums[idx])
            backtrack(idx+1)

            subsets.pop()
            backtrack(idx+1)
        backtrack(0)
        return res


            