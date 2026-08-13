class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ways = [[-1,0],[1,0],[0,-1],[0,1]]
        dp = {}
        def solve(r,c,prevVal):
            if (min(r,c)<0 or r>n-1 or c>m-1 or matrix[r][c]<=prevVal):
                return 0
            if (r,c,prevVal) in dp:
                return dp[(r,c,prevVal)]
            res = 1
            for way in ways:
                res = max(res,1 + solve(r+way[0],c+way[1],matrix[r][c]))
            dp[(r,c,prevVal)]  = res
            return res
        ans = 0
        for r in range(n):
            for c in range(m):
                ans = max(ans,solve(r,c,float('-inf')))
        return ans

        