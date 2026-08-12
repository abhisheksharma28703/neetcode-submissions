class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        def solve(i,j,k,dp):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            ans = False
            if i<len(s1) and s1[i] == s3[k]:
                ans = ans or solve(i+1,j,k+1,dp)
            if j<len(s2) and s2[j] == s3[k]:
                ans = ans or solve(i,j+1,k+1,dp)
            dp[(i,j,k)] = ans
            return ans
        return solve(0,0,0,dp)
       
        
                


        
        