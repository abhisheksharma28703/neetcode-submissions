class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binarySearch():
            left = 0
            right = len(arr)-1
            while left<=right:
                mid = (left+right)//2
                if arr[mid] < x:
                    left = mid+1
                else :
                    right = mid-1
            return left
        n = len(arr)
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[n-1]:
            return arr[n-k:]
        idx = binarySearch()
        l = idx-1
        r = idx
        count = 0
        while count<k :
            if l < 0:
                r += 1
                count += 1
                continue
            elif r >= n:
                l -= 1
                count += 1
                continue
            left_diff = abs(arr[l]-x)
            right_diff = abs(arr[r]-x)
            if left_diff<=right_diff:              
                l -= 1
            else:
                r += 1
            count += 1
        return arr[l+1:r]