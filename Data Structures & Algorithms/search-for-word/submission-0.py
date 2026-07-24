class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board[0])
        m = len(board)
        visited = [[False]*n for _ in range(m)]
        def backtrack(r,c,idx):
            if idx == len(word):
                return True
            if r<0 or c<0 or r>=m or c>=n :
                return False
            if visited[r][c] or board[r][c]!=word[idx]:
                return False
            visited[r][c] = True
            found = (backtrack(r+1,c,idx+1) or
                     backtrack(r-1,c,idx+1) or
                     backtrack(r,c+1,idx+1) or
                     backtrack(r,c-1,idx+1) )
            visited[r][c] = False
            return found
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        return False
        

        

