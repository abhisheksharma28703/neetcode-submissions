# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        q = deque()
        q.append(root)

        while q:
            temp = q.popleft()
            res.append(temp.val)

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        res.sort()
        return res[k-1]

            