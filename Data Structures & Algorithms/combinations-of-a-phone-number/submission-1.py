class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        c = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
            }      
        res = []
        def backtracking(idx,curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for char in c[digits[idx]]:
                backtracking(idx+1,curStr+char)
                
        if digits:
            backtracking(0,'')
        return res




        
