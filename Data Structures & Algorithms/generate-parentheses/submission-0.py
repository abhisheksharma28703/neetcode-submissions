class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(curr,opencount,closecount):
            if len(curr) == n*2:
                res.append(curr)
                return
            if opencount<n:
                backtracking(curr+'(',opencount+1,closecount)
            if closecount<opencount:
                backtracking(curr + ')',opencount,closecount+1)
            
        backtracking('',0,0)
        return res