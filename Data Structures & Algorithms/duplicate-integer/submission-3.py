class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash_map = []
        # for i in range(len(nums)):
        #     if nums[i] in hash_map:
        #         return True
        #     hash_map.append(nums[i])
        # return False
        dc = {}
        for i in range(len(nums)):
            dc[nums[i]] = dc.get(nums[i],0)+1
            
            if dc[nums[i]] > 1:
                return True
        return False
