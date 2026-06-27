class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for i in range(n):
            minHeight = float('inf')
            for j in range(i,n):
                minHeight = min(minHeight,heights[j])
                area = max(area,minHeight*(j-i+1))
        return area


            