class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = {}
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == m:
                return n-j
            if j == n:
                return m-i
            if word1[i] == word2[j]:
                dp[(i,j)] = solve(i+1,j+1)
            else:
                delete = solve(i+1,j)
                insert = solve(i,j+1)
                replace = solve(i+1,j+1)
                dp[(i,j)] = 1 + min(delete,insert,replace)
            return dp[(i,j)]
        return solve(0,0)
        