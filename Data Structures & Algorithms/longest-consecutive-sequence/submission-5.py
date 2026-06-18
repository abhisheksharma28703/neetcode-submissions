class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        copy = set(nums)

        for num in nums:
            streak = 0
            curr = num
            while curr in copy:
                streak += 1
                curr += 1
            res = max(streak,res)
        return res