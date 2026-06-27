class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i in range(n+1):
            cur_height = 0 if i==n else heights[i]

            while stack and heights[stack[-1]]>=cur_height:
                height = heights[stack.pop()]
            
                width = i if not stack else i-stack[-1]-1

                area = height*width
                maxArea = max(maxArea,area)
        
            stack.append(i)
        return maxArea