# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        def temp(root,maxSum):
            if not root:
                return 0
            left = max(0,temp(root.left,self.maxSum))
            right = max(0,temp(root.right,self.maxSum))

            self.maxSum = max(self.maxSum,left+right+root.val)
            return max(left,right)+root.val
        
        temp(root,self.maxSum)
        return self.maxSum
        
        