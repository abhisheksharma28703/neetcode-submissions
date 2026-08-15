class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)

        dp = {}
        def solve(l,r):
            if l+1 == r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            ans = 0
            for k in range(l+1,r):
                coins = arr[l]*arr[k]*arr[r] + solve(l,k) + solve(k,r)
                ans = max(coins,ans)
            dp[(l,r)] = ans
            return ans
        return solve(0,n-1)
        