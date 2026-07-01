class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = {}
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 1
            else:
                temp[nums[i]] += 1
        
        for values in temp:
            if temp[values] > 1:
                return values