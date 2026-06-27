class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        s = 0
        e = m*n-1

        while s<=e:
            mid = (s+e)//2
            row = mid//m
            col = mid%m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                e = mid -1
            else:
                s = mid + 1
        return False