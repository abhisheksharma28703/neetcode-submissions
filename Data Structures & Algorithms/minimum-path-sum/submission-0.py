class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1]*m for _ in range(n)]
        def solve(row,col):
            if row>=n or col>=m:
                return float('inf')
            if row == n-1 and col == m-1:
                return grid[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            dp[row][col] = grid[row][col] + min(solve(row+1,col),solve(row,col+1))
            return dp[row][col]
        return solve(0,0)

            
