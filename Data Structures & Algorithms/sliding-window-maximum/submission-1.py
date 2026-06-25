class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            temp = float('-inf')
            for  j in range(i ,i+k):
                temp = max(temp,nums[j])
            ans.append(temp)
        return ans