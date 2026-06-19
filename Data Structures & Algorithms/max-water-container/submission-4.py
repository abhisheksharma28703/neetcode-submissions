class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final = 0
        n = len(heights)
        left = 0
        right = n-1

        while(left<right):
            area = min(heights[left],heights[right])*(right-left)
            final = max(final,area)
            if(max(heights[left],heights[right])==heights[left]):
                right -= 1
            else:
                left += 1
        return final
