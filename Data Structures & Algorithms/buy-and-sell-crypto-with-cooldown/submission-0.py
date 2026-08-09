class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## we will be maintaining a dict 
        ## in which key = (i,buying) and val = max_profit
        dp = {}
        
        def solve(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            if buying:
                buy = solve(i+1,not buying) - prices[i]
                cooldown = solve(i+1,buying)
                dp[(i,buying)] = max(buy,cooldown)
            else:
                sell = solve(i+2,not buying) + prices[i]
                cooldown = solve(i+1,buying)
                dp[(i,buying)] = max(cooldown,sell)
            return dp[(i,buying)]
        return solve(0,True)

                


