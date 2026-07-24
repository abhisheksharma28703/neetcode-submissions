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
        tp = []
        for i in digits:
            tp.append(c[i])
        res = []
        temp1 = []
        def backtracking(idx):
            if idx == len(tp):
                res.append(''.join(temp1))
                return
            for char in tp[idx]:
                temp1.append(char)
                backtracking(idx+1)
                temp1.pop()
        backtracking(0)
        return res




        
