class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            n = len(heights)
            stack = [] 
            leftmost = [-1]*n
            rightmost = [n]*n

            for i in range(n):
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    leftmost[i] = stack[-1]
                stack.append(i)

            while len(stack)!=0:
                stack.pop()
            
            for i in range(n-1,-1,-1):
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:    
                    rightmost[i] = stack[-1]
                stack.append(i)
            maxArea = 0
            for i in range(n):
                width = rightmost[i]-leftmost[i]-1
                height = heights[i]
                maxArea = max(maxArea,height*width)
            
            return maxArea


            

