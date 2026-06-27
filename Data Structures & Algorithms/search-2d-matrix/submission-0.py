class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        n = len(matrix)
        m = len(matrix[0])
        r = n - 1

        temp = [i for row in matrix for i in row]

        l = 0
        r = len(temp)-1

        while l<=r:
            mid = (l+r)//2

            if temp[mid] == target:
                return True
            elif temp[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return False