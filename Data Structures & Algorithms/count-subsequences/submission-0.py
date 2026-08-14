class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        n = len(s)
        def solve(idx,substring):
            if substring == t:
                return 1
            if (idx,substring) in dp:
                return dp[(idx,substring)]
            if idx >= n:
                return 0
            
            pick = solve(idx+1,substring + s[idx])
            notpick = solve(idx+1,substring)
            dp[(idx,substring)] = pick + notpick
            return dp[(idx,substring)]
        return solve(0,'')

        